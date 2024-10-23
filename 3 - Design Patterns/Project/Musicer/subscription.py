from abc import ABC, abstractmethod
import logging

class Subscription(ABC):
    @abstractmethod
    def stream(self):
        pass

class FreeSubscription(Subscription):
    def __init__(self):
        self.name = "Free Tier"
        
    def stream(self):
        logging.info("Streaming in low quality, with ads.")

class PremiumSubscription(Subscription):
    def __init__(self):
        self.name = "Premium Tier"

    def stream(self):
        logging.info("Streaming in high quality, with no ads.")

