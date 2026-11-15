import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from reliable import Store

class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.store = Store(Path(self.tmp.name) / "jobs.sqlite")

    def tearDown(self):
        self.tmp.cleanup()

    def test_duplicate_enqueue(self):
        self.assertEqual(self.store.enqueue("a"), "pending")
        self.assertEqual(self.store.enqueue("a"), "pending")
        self.assertEqual(self.store.get("a")["attempt"], 0)

    def test_claim_once_concurrent(self):
        self.store.enqueue("a")
        with ThreadPoolExecutor(max_workers=8) as pool:
            outcomes = list(pool.map(lambda _: self.store.claim("a"), range(24)))
        self.assertEqual(sum(outcomes), 1)
        self.assertEqual(self.store.get("a")["attempt"], 1)

    def test_verified_requires_receipt(self):
        self.store.enqueue("a")
        self.store.claim("a")
        with self.assertRaises(ValueError):
            self.store.verify("a", "")
        self.assertTrue(self.store.verify("a", "receipt-001"))
        self.assertFalse(self.store.verify("a", "receipt-002"))
        self.assertEqual(self.store.get("a")["receipt"], "receipt-001")

    def test_unknown_not_retried_automatically(self):
        self.store.enqueue("a")
        self.store.claim("a")
        self.assertTrue(self.store.mark_unknown("a"))
        self.assertFalse(self.store.claim("a"))
        self.assertEqual(self.store.get("a")["state"], "unknown")

    def test_unclaimed_cannot_verify(self):
        self.store.enqueue("a")
        self.assertFalse(self.store.verify("a", "r"))

    def test_reopen_persists(self):
        self.store.enqueue("a")
        self.store.claim("a")
        self.store.mark_unknown("a")
        self.assertEqual(Store(self.store.path).get("a")["state"], "unknown")

    def test_unknown_is_terminal_for_verification(self):
        self.store.enqueue("job")
        self.store.claim("job")
        self.store.mark_unknown("job")
        self.assertFalse(self.store.verify("job", "late-receipt"))

    def test_verified_cannot_be_marked_unknown(self):
        self.store.enqueue("job")
        self.store.claim("job")
        self.store.verify("job", "receipt")
        self.assertFalse(self.store.mark_unknown("job"))

    def test_duplicate_enqueue_does_not_reset_verified(self):
        self.store.enqueue("job")
        self.store.claim("job")
        self.store.verify("job", "receipt")
        self.assertEqual(self.store.enqueue("job"), "verified")
        self.assertEqual(self.store.get("job")["receipt"], "receipt")

    def test_missing_job_cannot_be_claimed(self):
        self.assertFalse(self.store.claim("missing"))

    def test_receipt_is_unverified_caller_assertion(self):
        self.store.enqueue("job")
        self.store.claim("job")
        self.assertTrue(self.store.verify("job", "not-a-provider-validated-receipt"))

if __name__ == "__main__":
    unittest.main()
