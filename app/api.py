from fastapi import APIRouter, HTTPException

from app.agent import run_growth_agent
from app.agentic_agent import run_agentic_growth_agent
from app.actions import create_payment_link
from app.guardrails import validate_opportunity
from app.tools import analyze_merchant, find_growth_opportunity


router = APIRouter()


@router.get("/")
def root():
    return {
        "name": "RazorGrowth",
        "description": "Agentic Merchant Growth Engine",
        "status": "running",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
    }


@router.get("/merchant/analyze")
def merchant_analysis():
    return analyze_merchant()


@router.get("/merchant/opportunity")
def growth_opportunity():
    return find_growth_opportunity()


@router.post("/agent/analyze")
def agent_analysis():
    """
    Run the original deterministic growth agent.
    """

    try:
        return run_growth_agent()

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.post("/agent/agentic-analyze")
def agentic_analysis():
    """
    Run the RazorGrowth agentic workflow.

    The agent analyzes merchant data, discovers available
    growth opportunities, compares them, and returns the
    strongest next-best action.
    """

    try:
        return run_agentic_growth_agent()

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.post("/action/payment-link")
def payment_link_action(
    approved: bool = False,
):
    """
    Execute the recommended payment-link action only
    after explicit merchant approval.

    This endpoint uses the deterministic opportunity engine.
    """

    if not approved:
        return {
            "success": False,
            "status": "approval_required",
            "message": (
                "Merchant approval is required before creating "
                "a Razorpay payment link."
            ),
        }

    opportunity = find_growth_opportunity()

    guardrail_result = validate_opportunity(opportunity)

    if not guardrail_result["valid"]:
        return {
            "success": False,
            "status": "blocked_by_guardrail",
            "guardrail": guardrail_result,
        }

    payment_result = create_payment_link(
        amount=opportunity["target_product_price"],
        description=(
            "RazorGrowth cross-sell offer: "
            + opportunity["target_product"]
        ),
    )

    return {
        "action": "create_payment_link",
        "opportunity": opportunity,
        "guardrail": guardrail_result,
        "payment_result": payment_result,
    }


@router.post("/agent/execute")
def execute_agent_action(
    approved: bool = False,
):
    """
    Execute the agent's recommended action only after
    guardrail validation and explicit merchant approval.
    """

    try:
        # Step 1: Ask the agent for the best recommendation.
        result = run_agentic_growth_agent()

        recommendation = result.get(
            "recommendation",
            {},
        )

        if not recommendation:
            return {
                "success": False,
                "status": "no_recommendation",
                "message": (
                    "Agent did not return a recommendation."
                ),
            }

        # Step 2: Validate the recommendation.
        validation = validate_opportunity(
            recommendation
        )

        if not validation["valid"]:
            return {
                "success": False,
                "status": "blocked_by_guardrail",
                "guardrail": validation,
                "recommendation": recommendation,
            }

        # Step 3: Require explicit merchant approval.
        if not approved:
            return {
                "success": False,
                "status": "approval_required",
                "message": (
                    "Merchant approval is required before "
                    "executing the recommended action."
                ),
                "recommendation": recommendation,
                "guardrail": validation,
            }

        # Step 4: Execute the approved action.
        if recommendation.get(
            "recommended_action"
        ) != "create_payment_link":
            return {
                "success": False,
                "status": "unsupported_action",
                "message": (
                    "The recommended action is not supported "
                    "by the execution layer."
                ),
                "recommendation": recommendation,
            }

        payment_result = create_payment_link(
            amount=recommendation[
                "target_product_price"
            ],
            description=(
                "RazorGrowth cross-sell offer: "
                + recommendation["target_product"]
            ),
        )

        return {
            "success": payment_result.get(
                "success",
                False,
            ),
            "status": (
                "executed"
                if payment_result.get("success")
                else "action_failed"
            ),
            "agent_result": result,
            "guardrail": validation,
            "payment_result": payment_result,
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )
