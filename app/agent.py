from app.tools import analyze_merchant, find_growth_opportunity


def run_growth_agent():
    merchant = analyze_merchant()
    opportunity = find_growth_opportunity()

    return {
        "agent": "RazorGrowth",
        "merchant_analysis": merchant,
        "growth_opportunity": opportunity,
        "recommended_action": opportunity.get("recommended_action"),
        "status": "success",
    }