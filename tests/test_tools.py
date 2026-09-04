from app.tools import analyze_merchant, find_growth_opportunity


def test_analyze_merchant():
    result = analyze_merchant()

    assert result["total_orders"] == 17
    assert result["total_customers"] == 10
    assert result["total_revenue"] == 21383.0
    assert result["customers_with_orders"] == 10

    assert len(result["top_products"]) > 0
    assert result["top_products"][0]["name"] == "Pro Analytics"


def test_find_growth_opportunity():
    result = find_growth_opportunity()

    assert result["opportunity_type"] == "cross_sell"
    assert result["anchor_product"] == "Pro Analytics"
    assert result["target_product"] == "Annual Pro Upgrade"
    assert result["target_product_price"] == 2499.0
    assert result["eligible_customer_count"] == 6
    assert result["revenue_potential"] == 14994.0
    assert result["recommended_action"] == "create_payment_link"
    assert len(result["eligible_customer_ids"]) == 6