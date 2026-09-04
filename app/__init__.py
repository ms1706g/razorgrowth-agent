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


def find_growth_opportunity():
    connection = get_connection()

    eligible_customers = connection.execute(
        """
        SELECT DISTINCT c.id, c.name, c.email
        FROM customers c
        JOIN orders o ON o.customer_id = c.id
        WHERE o.product_id = 1
          AND c.id NOT IN (
              SELECT customer_id
              FROM orders
              WHERE product_id = 2
          )
        """
    ).fetchall()

    product = connection.execute(
        """
        SELECT name, price
        FROM products
        WHERE id = 2
        """
    ).fetchone()

    connection.close()

    customer_ids = [row["id"] for row in eligible_customers]

    return {
        "opportunity_type": "cross_sell",
        "target_product": product["name"],
        "target_product_price": product["price"],
        "eligible_customer_count": len(customer_ids),
        "eligible_customer_ids": customer_ids,
        "reason": (
            f"{len(customer_ids)} customers purchased Pro Analytics "
            f"but have not purchased {product['name']}."
        ),
        "recommended_action": "create_payment_link",
    }