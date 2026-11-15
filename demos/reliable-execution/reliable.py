"""A minimal, auditable SQLite task runner with explicit uncertainty."""
import sqlite3
from pathlib import Path

SCHEMA = """CREATE TABLE IF NOT EXISTS jobs (
  id TEXT PRIMARY KEY,
  state TEXT NOT NULL CHECK(state IN ('pending','claimed','verified','unknown')),
  attempt INTEGER NOT NULL DEFAULT 0,
  receipt TEXT,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);"""

class Store:
    def __init__(self, path):
        self.path = str(Path(path))
        with self.connect() as db:
            db.execute(SCHEMA)

    def connect(self):
        db = sqlite3.connect(self.path, timeout=5, isolation_level=None)
        db.execute("PRAGMA busy_timeout=5000")
        return db

    def enqueue(self, job_id):
        with self.connect() as db:
            db.execute("INSERT OR IGNORE INTO jobs(id,state) VALUES (?,?)", (job_id, "pending"))
            return db.execute("SELECT state FROM jobs WHERE id=?", (job_id,)).fetchone()[0]

    def claim(self, job_id):
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            changed = db.execute("UPDATE jobs SET state='claimed',attempt=attempt+1,updated_at=CURRENT_TIMESTAMP WHERE id=? AND state='pending'", (job_id,)).rowcount
            db.execute("COMMIT")
            return bool(changed)

    def verify(self, job_id, receipt):
        if not receipt:
            raise ValueError("nonempty receipt required")
        with self.connect() as db:
            return bool(db.execute("UPDATE jobs SET state='verified',receipt=?,updated_at=CURRENT_TIMESTAMP WHERE id=? AND state='claimed'", (receipt,job_id)).rowcount)

    def mark_unknown(self, job_id):
        with self.connect() as db:
            return bool(db.execute("UPDATE jobs SET state='unknown',updated_at=CURRENT_TIMESTAMP WHERE id=? AND state='claimed'", (job_id,)).rowcount)

    def get(self, job_id):
        with self.connect() as db:
            row = db.execute("SELECT id,state,attempt,receipt FROM jobs WHERE id=?", (job_id,)).fetchone()
            return dict(zip(("id","state","attempt","receipt"),row)) if row else None
