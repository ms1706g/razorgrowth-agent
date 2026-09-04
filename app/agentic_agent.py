import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.tools import (
    analyze_merchant,
    find_growth_opportunities,
)

load_dotenv()


TOOLS = {
    "analyze_merchant": analyze_merchant,
    "find_growth_opportunities": find_growth_opportunities,
}


TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "analyze_merchant",
            "description": (
                "Analyze overall merchant performance including revenue, "
                "orders, customers, and product performance."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "find_growth_opportunities",
            "description": (
                "Find all viable merchant growth opportunities. "
                "Return the available opportunities with anchor products, "
                "target products, eligible customers, revenue potential, "
                "and recommended actions so the agent can compare them "
                "and select the strongest one."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
]


SYSTEM_PROMPT = """
You are RazorGrowth, an AI merchant growth agent.

Your job is to analyze merchant data and identify the strongest
next-best growth action.

Use the available tools to gather evidence before making a recommendation.

You have access to multiple growth opportunities. Do not assume that
the first opportunity returned is the best one. Compare the available
opportunities using merchant evidence and choose the strongest one.

Prioritize:
1. Revenue potential
2. Number of eligible customers
3. Product relevance
4. A clear, actionable next step

Do not invent merchant metrics, customers, products, prices, or opportunities.

Your final response MUST be valid JSON with exactly these fields:

{
  "opportunity_type": "...",
  "anchor_product": "...",
  "target_product": "...",
  "target_product_price": 0,
  "eligible_customer_count": 0,
  "eligible_customer_ids": [],
  "revenue_potential": 0,
  "why_this_opportunity": "...",
  "recommended_action": "...",
  "guardrail_required": true
}

Rules:
- Use only facts returned by the tools.
- Select the opportunity with the strongest evidence.
- revenue_potential must come from the available opportunity data.
- eligible_customer_ids must come from the selected opportunity.
- target_product_price must come from the selected opportunity.
- recommended_action must come from the selected opportunity.
- Explain why the selected opportunity is stronger than the alternatives.
- guardrail_required must always be true for an action that can affect a merchant.
"""


def fallback_response(reason):
    """
    Safe fallback used when the LLM is unavailable.

    The fallback still behaves like a decision workflow:
    1. Discover all growth opportunities.
    2. Rank them by revenue potential.
    3. Select the strongest opportunity.
    4. Return the decision trace.
    """

    opportunities = find_growth_opportunities()

    if not opportunities:
        return {
            "agent": "RazorGrowth",
            "mode": "safe_fallback",
            "status": "success",
            "reason": reason,
            "tool_trace": [
                {
                    "tool": "find_growth_opportunities",
                    "result": [],
                }
            ],
            "recommendation": {
                "opportunity_type": "none",
                "anchor_product": None,
                "target_product": None,
                "target_product_price": None,
                "eligible_customer_count": 0,
                "eligible_customer_ids": [],
                "revenue_potential": 0,
                "why_this_opportunity": (
                    "No viable growth opportunity was identified."
                ),
                "recommended_action": None,
                "guardrail_required": True,
            },
        }

    selected = max(
        opportunities,
        key=lambda opportunity: opportunity["revenue_potential"],
    )

    ranked_opportunities = sorted(
        opportunities,
        key=lambda opportunity: opportunity["revenue_potential"],
        reverse=True,
    )

    return {
        "agent": "RazorGrowth",
        "mode": "safe_fallback",
        "status": "success",
        "reason": reason,
        "tool_trace": [
            {
                "tool": "find_growth_opportunities",
                "result": opportunities,
            },
            {
                "decision": "select_highest_revenue_potential",
                "selected_product": selected["target_product"],
                "selected_revenue_potential": selected[
                    "revenue_potential"
                ],
                "ranked_products": [
                    {
                        "product": opportunity["target_product"],
                        "revenue_potential": opportunity[
                            "revenue_potential"
                        ],
                    }
                    for opportunity in ranked_opportunities
                ],
            },
        ],
        "recommendation": {
            "opportunity_type": selected["opportunity_type"],
            "anchor_product": selected.get("anchor_product"),
            "target_product": selected["target_product"],
            "target_product_price": selected["target_product_price"],
            "eligible_customer_count": selected[
                "eligible_customer_count"
            ],
            "eligible_customer_ids": selected[
                "eligible_customer_ids"
            ],
            "revenue_potential": selected["revenue_potential"],
            "why_this_opportunity": (
                f"Selected because it has the highest estimated "
                f"revenue potential among the discovered opportunities: "
                f"₹{selected['revenue_potential']:.2f}."
            ),
            "recommended_action": selected["recommended_action"],
            "guardrail_required": True,
        },
    }


def parse_recommendation(content):
    """
    Convert the LLM's final response into structured recommendation data.
    """

    if not content:
        raise ValueError("Agent returned an empty recommendation.")

    try:
        recommendation = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError(
            "Agent returned a non-JSON recommendation."
        )

    required_fields = {
        "opportunity_type",
        "anchor_product",
        "target_product",
        "target_product_price",
        "eligible_customer_count",
        "eligible_customer_ids",
        "revenue_potential",
        "why_this_opportunity",
        "recommended_action",
        "guardrail_required",
    }

    missing = required_fields - set(recommendation.keys())

    if missing:
        raise ValueError(
            "Agent recommendation missing fields: {}".format(
                ", ".join(sorted(missing))
            )
        )

    return recommendation


def run_agentic_growth_agent():
    """
    Run the RazorGrowth agent.

    If an OpenAI API key is available, the agent uses LLM tool calling.
    If the LLM is unavailable, the system safely falls back to the
    deterministic multi-opportunity decision workflow.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return fallback_response(
            "OPENAI_API_KEY is not configured."
        )

    client = OpenAI(api_key=api_key)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": (
                "Analyze this merchant, inspect all available growth "
                "opportunities, compare them, and determine the strongest "
                "next-best action."
            ),
        },
    ]

    tool_trace = []

    try:
        for _ in range(5):
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=messages,
                tools=TOOL_DEFINITIONS,
                tool_choice="auto",
            )

            message = response.choices[0].message

            assistant_message = {
                "role": "assistant",
                "content": message.content,
            }

            if message.tool_calls:
                assistant_message["tool_calls"] = [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments,
                        },
                    }
                    for tool_call in message.tool_calls
                ]

            messages.append(assistant_message)

            if not message.tool_calls:
                recommendation = parse_recommendation(
                    message.content
                )

                return {
                    "agent": "RazorGrowth",
                    "mode": "llm_tool_calling",
                    "status": "success",
                    "tool_trace": tool_trace,
                    "recommendation": recommendation,
                }

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name

                if tool_name not in TOOLS:
                    raise ValueError(
                        "Unknown tool requested: {}".format(
                            tool_name
                        )
                    )

                arguments = tool_call.function.arguments or "{}"

                try:
                    json.loads(arguments)
                except json.JSONDecodeError:
                    arguments = "{}"

                result = TOOLS[tool_name]()

                tool_trace.append(
                    {
                        "tool": tool_name,
                        "result": result,
                    }
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result),
                    }
                )

        raise RuntimeError(
            "Agent exceeded maximum tool-calling steps."
        )

    except Exception as exc:
        error_text = str(exc)

        if "429" in error_text or "quota" in error_text.lower():
            return fallback_response(
                "LLM unavailable: API quota or credits exhausted."
            )

        return fallback_response(
            "LLM unavailable: {}".format(error_text)
        )
