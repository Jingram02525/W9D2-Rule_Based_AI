# tests/test_payment_action.py
import unittest
from src.rules import payment_action

class TestPaymentAction(unittest.TestCase):
    # Rule 1
    def test_saved_valid(self):
        self.assertEqual(
            payment_action(use_saved=True, payment_valid=True),
            "Use the saved payment method"
        )

    # Rule 2
    def test_saved_invalid(self):
        self.assertEqual(
            payment_action(use_saved=True, payment_valid=False),
            "Prompt customer to edit or select another method"
        )

    # Rule 3
    def test_credit_card(self):
        self.assertEqual(
            payment_action(use_saved=False, new_payment_type="Credit Card"),
            "Obtain card information"
        )

    # Rule 4
    def test_gift_card_sufficient(self):
        self.assertEqual(
            payment_action(use_saved=False, new_payment_type="Gift Card", funds_sufficient=True),
            "Use gift card"
        )

    # Rule 5
    def test_gift_card_insufficient(self):
        self.assertEqual(
            payment_action(use_saved=False, new_payment_type="Gift Card", funds_sufficient=False),
            "Ask for secondary payment method"
        )

    # Rule 6
    def test_paypal(self):
        self.assertEqual(
            payment_action(use_saved=False, new_payment_type="PayPal"),
            "Link to PayPal to complete"
        )

    # Default
    def test_default_unknown_type(self):
        self.assertEqual(
            payment_action(use_saved=False, new_payment_type="Crypto"),
            "Prompt customer to edit or select another method"
        )

if __name__ == "__main__":
    unittest.main()
