import requests

from app.config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET


RAZORPAY_PAYMENT_LINK_URL = "https://api.razorpay.com/v1/payment_links"


def create_payment_link(
    amount,
    description,
    customer_name=None,
    customer_email=None,
    customer_contact=None,
):
    """
    Create a Razorpay Payment Link using the configured
    Razorpay test credentials.
    """

    if not RAZORPAY_KEY_ID or not RAZORPAY_KEY_SECRET:
        return {
            "success": False,
            "message": "Razorpay credentials are not configured.",
        }

    if amount <= 0:
        return {
            "success": False,
            "message": "Payment amount must be greater than zero.",
        }

    payload = {
        "amount": int(round(amount * 100)),
        "currency": "INR",
        "description": description,
    }

    customer = {}

    if customer_name:
        customer["name"] = customer_name

    if customer_email:
        customer["email"] = customer_email

    if customer_contact:
        customer["contact"] = customer_contact

    if customer:
        payload["customer"] = customer

    try:
        response = requests.post(
            RAZORPAY_PAYMENT_LINK_URL,
            auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET),
            json=payload,
            timeout=15,
        )

        if response.status_code >= 400:
            return {
                "success": False,
                "message": "Razorpay API request failed.",
                "status_code": response.status_code,
                "details": response.text,
            }

        data = response.json()

        return {
            "success": True,
            "message": "Razorpay payment link created successfully.",
            "payment_link_id": data.get("id"),
            "short_url": data.get("short_url"),
            "amount": amount,
            "currency": "INR",
        }

    except requests.RequestException as exc:
        return {
            "success": False,
            "message": "Unable to reach Razorpay API.",
            "details": str(exc),
        }