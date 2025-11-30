# src/rules.py

def payment_action(
    use_saved: bool,
    payment_valid: bool | None = None,
    new_payment_type: str | None = None,
    funds_sufficient: bool | None = None,
) -> str:
    """
    Decide the next action for checkout, based on the decision table.

    Conditions (from your table)
    - use_saved: customer chooses to use saved payment method (True/False)
    - payment_valid: saved method is valid (True/False) — only relevant when use_saved is True
    - new_payment_type: one of {"credit card", "gift card", "paypal"} — used when use_saved is False
    - funds_sufficient: gift-card balance covers cost (True/False) — only relevant for gift cards

    Outcomes
    - "Use the saved payment method"                    (OC001)
    - "Prompt customer to edit or select another method" (OC002)
    - "Obtain card information"                         (OC003)
    - "Use gift card"                                   (OC004)
    - "Ask for secondary payment method"                (OC005)
    - "Link to PayPal to complete"                      (OC006)
    - Default: prompt to choose a method safely

    Returns: one of the strings above.
    """

    # Normalize strings early
    t = (new_payment_type or "").strip().lower()

    # Rules 1–2: Using a saved method
    if use_saved is True:
        if payment_valid is True:
            return "Use the saved payment method"                    # OC001 (Rule 1)
        else:
            return "Prompt customer to edit or select another method" # OC002 (Rule 2)

    # From here on, we are NOT using a saved method; pick based on the new type
    if t == "credit card":
        return "Obtain card information"                               # OC003 (Rule 3)

    if t == "gift card":
        if funds_sufficient is True:
            return "Use gift card"                                     # OC004 (Rule 4)
        else:
            return "Ask for secondary payment method"                  # OC005 (Rule 5)

    if t == "paypal":
        return "Link to PayPal to complete"                            # OC006 (Rule 6)

    # Safe default
    return "Prompt customer to edit or select another method"
