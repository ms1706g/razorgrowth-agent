from app.tools import analyze_merchant, find_growth_opportunity

def test_analyze_merchant():
    result = analyze_merchant()
    assert result['total_orders'] == 17
    assert result['total_customers'] == 10
    assert result['total_revenue'] > 0

def test_find_growth_opportunity():
    result = find_growth_opportunity()
    assert result['opportunity_type'] == 'cross_sell'
    assert result['recommended_action'] == 'create_payment_link'
    assert result['eligible_customer_count'] > 0
