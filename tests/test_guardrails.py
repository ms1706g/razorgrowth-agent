from app.guardrails import validate_opportunity


def test_valid_opportunity_passes():
    opportunity = {
        "opportunity_type": "cross_sell",
        "anchor_product": "Pro Analytics",
        "target_product": "Annual Pro Upgrade",
        "target_product_price": 2499.0,
        "eligible_customer_count": 6,
        "eligible_customer_ids": [1, 2, 4, 5, 8, 10],
        "revenue_potential": 14994.0,
        "recommended_action": "create_payment_link",
    }

    result = validate_opportunity(opportunity)

    assert result["valid"] is True
    assert result["reason"] == "Opportunity passed all guardrail checks."


def test_invalid_opportunity_is_blocked():
    opportunity = {
        "opportunity_type": "cross_sell",
        "target_product": "Annual Pro Upgrade",
        "target_product_price": -2499.0,
        "eligible_customer_count": 0,
        "eligible_customer_ids": [],
        "revenue_potential": 0,
        "recommended_action": "create_payment_link",
    }

    result = validate_opportunity(opportunity)

    assert result["valid"] is False