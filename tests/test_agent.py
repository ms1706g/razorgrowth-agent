from app.agent import run_growth_agent


def test_growth_agent_returns_successful_recommendation():
    result = run_growth_agent()

    assert result["agent"] == "RazorGrowth"
    assert result["status"] == "success"

    assert result["recommended_action"] == "create_payment_link"

    assert result["growth_opportunity"]["opportunity_type"] == "cross_sell"
    assert result["growth_opportunity"]["target_product"] == "Annual Pro Upgrade"
    assert result["growth_opportunity"]["eligible_customer_count"] == 6

    assert result["guardrail"]["valid"] is True