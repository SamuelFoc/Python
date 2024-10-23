import unittest
import logging
from Musicer.subscription import FreeSubscription, PremiumSubscription

class TestSubscription(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configure logging before running tests
        logging.basicConfig(level=logging.INFO)

    def setUp(self):
        self.free_subscription = FreeSubscription()
        self.premium_subscription = PremiumSubscription()

    def test_free_subscription(self):
        with self.assertLogs(level='INFO') as log:
            self.free_subscription.stream()
        self.assertIn("Streaming in low quality, with ads.", log.output[0])

    def test_premium_subscription(self):
        with self.assertLogs(level='INFO') as log:
            self.premium_subscription.stream()
        self.assertIn("Streaming in high quality, with no ads.", log.output[0])

if __name__ == "__main__":
    unittest.main()
