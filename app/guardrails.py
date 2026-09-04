ALLOWED_OPPORTUNITY_TYPES = {
    "cross_sell",
}

ALLOWED_ACTIONS = {
    "create_payment_link",
}


def validate_opportunity(opportunity):
    """
    Validate a growth opportunity before it becomes
    a merchant-facing recommendation.
    """

    if not opportunity:
        return {
            "valid": False,
            "reason": "No growth opportunity was identified.",
        }

    opportunity_type = opportunity.get("opportunity_type")
    if opportunity_type not in ALLOWED_OPPORTUNITY_TYPES:
        return {
            "valid": False,
            "reason": f"Unsupported opportunity type: {opportunity_type}",
        }

    target_product = opportunity.get("target_product")
    if not target_product:
        return {
            "valid": False,
            "reason": "Target product is required.",
        }

    target_price = opportunity.get("target_product_price")
    if target_price is None or target_price <= 0:
        return {
            "valid": False,
            "reason": "Target product price must be greater than zero.",
        }

    eligible_customer_count = opportunity.get("eligible_customer_count", 0)
    if eligible_customer_count <= 0:
        return {
            "valid": False,
            "reason": "No eligible customers were identified.",
        }

    recommended_action = opportunity.get("recommended_action")
    if recommended_action not in ALLOWED_ACTIONS:
        return {
            "valid": False,
            "reason": f"Unsupported recommended action: {recommended_action}",
        }

    revenue_potential = opportunity.get("revenue_potential", 0)
    if revenue_potential < 0:
        return {
            "valid": False,
            "reason": "Revenue potential cannot be negative.",
        }

    return {
        "valid": True,
        "reason": "Opportunity passed all guardrail checks.",
    }