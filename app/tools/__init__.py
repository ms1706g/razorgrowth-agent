from app.database import get_connection


def analyze_merchant():
    connection = get_connection()

    revenue = connection.execute(
        "SELECT COALESCE(SUM(amount), 0) AS revenue FROM orders"
    ).fetchone()["revenue"]

    orders = connection.execute(
        "SELECT COUNT(*) AS count FROM orders"
    ).fetchone()["count"]

    customers = connection.execute(
        "SELECT COUNT(*) AS count FROM customers"
    ).fetchone()["count"]

    successful_customers = connection.execute(
        """
        SELECT COUNT(DISTINCT customer_id) AS count
        FROM orders
        """
    ).fetchone()["count"]

    top_products = connection.execute(
        """
        SELECT
            p.name,
            COUNT(o.id) AS order_count,
            SUM(o.amount) AS revenue
        FROM orders o
        JOIN products p ON p.id = o.product_id
        GROUP BY p.id
        ORDER BY revenue DESC
        """
    ).fetchall()

    connection.close()

    return {
        "total_revenue": round(revenue, 2),
        "total_orders": orders,
        "total_customers": customers,
        "customers_with_orders": successful_customers,
        "top_products": [
            {
                "name": row["name"],
                "orders": row["order_count"],
                "revenue": round(row["revenue"], 2),
            }
            for row in top_products
        ],
    }


def find_growth_opportunities():
    """
    Return all viable cross-sell opportunities so the agent
    can compare them and choose the strongest one.
    """

    connection = get_connection()

    products = connection.execute(
        """
        SELECT
            p.id,
            p.name,
            p.price,
            COUNT(o.id) AS order_count,
            COALESCE(SUM(o.amount), 0) AS revenue
        FROM products p
        LEFT JOIN orders o ON o.product_id = p.id
        GROUP BY p.id
        ORDER BY revenue DESC
        """
    ).fetchall()

    if len(products) < 2:
        connection.close()
        return []

    anchor_product = products[0]
    opportunities = []

    for candidate in products[1:]:
        eligible_customers = connection.execute(
            """
            SELECT DISTINCT c.id
            FROM customers c
            JOIN orders anchor_order
                ON anchor_order.customer_id = c.id
            WHERE anchor_order.product_id = ?
              AND c.id NOT IN (
                  SELECT customer_id
                  FROM orders
                  WHERE product_id = ?
              )
            """,
            (anchor_product["id"], candidate["id"]),
        ).fetchall()

        eligible_count = len(eligible_customers)

        if eligible_count <= 0:
            continue

        revenue_potential = eligible_count * candidate["price"]

        opportunities.append(
            {
                "opportunity_type": "cross_sell",
                "anchor_product": anchor_product["name"],
                "target_product": candidate["name"],
                "target_product_price": candidate["price"],
                "eligible_customer_count": eligible_count,
                "eligible_customer_ids": [
                    row["id"] for row in eligible_customers
                ],
                "revenue_potential": round(revenue_potential, 2),
                "recommended_action": "create_payment_link",
                "reason": (
                    f"{eligible_count} customers purchased "
                    f"{anchor_product['name']} but have not purchased "
                    f"{candidate['name']}."
                ),
            }
        )

    connection.close()

    return opportunities


def find_growth_opportunity():
    """
    Keep the existing API contract by returning the
    highest-revenue opportunity.
    """

    opportunities = find_growth_opportunities()

    if not opportunities:
        return {
            "opportunity_type": "none",
            "target_product": None,
            "target_product_price": None,
            "eligible_customer_count": 0,
            "eligible_customer_ids": [],
            "reason": "No viable cross-sell opportunity found.",
            "recommended_action": None,
            "revenue_potential": 0,
        }

    return max(
        opportunities,
        key=lambda opportunity: opportunity["revenue_potential"],
    )