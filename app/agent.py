from app.tools import analyze_merchant, find_growth_opportunity
from app.guardrails import validate_opportunity


def run_growth_agent():
    """
    Deterministic baseline growth agent.

    Analyzes merchant performance, identifies the strongest
    growth opportunity, validates it through guardrails, and
    returns a structured recommendation.
    """

    merchant = analyze_merchant()
    opportunity = find_growth_opportunity()

    # Handle cases where no valid opportunity exists.
    if not opportunity:
        return {
            "agent": "RazorGrowth",
            "merchant_analysis": merchant,
            "growth_opportunity": None,
            "recommended_action": None,
            "status": "no_opportunity",
            "guardrail": {
                "valid": False,
                "reason": "No viable growth opportunity was identified.",
            },
        }

    guardrail_result = validate_opportunity(opportunity)

    if not guardrail_result["valid"]:
        return {
            "agent": "RazorGrowth",
            "merchant_analysis": merchant,
            "growth_opportunity": opportunity,
            "recommended_action": None,
            "status": "blocked",
            "guardrail": guardrail_result,
        }

    return {
        "agent": "RazorGrowth",
        "merchant_analysis": merchant,
        "growth_opportunity": opportunity,
        "recommended_action": opportunity.get("recommended_action"),
        "status": "success",
        "guardrail": guardrail_result,
    }