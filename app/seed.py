from datetime import datetime, timedelta

from app.database import get_connection, initialize_database


def seed_database():
    initialize_database()

    connection = get_connection()

    # Avoid duplicate seed data
    existing = connection.execute(
        "SELECT COUNT(*) AS count FROM customers"
    ).fetchone()["count"]

    if existing > 0:
        print("Database already contains data. Skipping seed.")
        connection.close()
        return

    customers = [
        (1, "Aarav Mehta", "aarav@example.com", 4, 5200, 7),
        (2, "Isha Sharma", "isha@example.com", 3, 3900, 12),
        (3, "Rohan Kapoor", "rohan@example.com", 6, 8400, 4),
        (4, "Ananya Singh", "ananya@example.com", 2, 2400, 35),
        (5, "Vivaan Gupta", "vivaan@example.com", 5, 6700, 9),
        (6, "Diya Verma", "diya@example.com", 3, 4100, 42),
        (7, "Kabir Jain", "kabir@example.com", 7, 9800, 6),
        (8, "Meera Shah", "meera@example.com", 2, 2600, 28),
        (9, "Arjun Malhotra", "arjun@example.com", 4, 5800, 14),
        (10, "Sara Khan", "sara@example.com", 5, 7200, 5),
    ]

    products = [
        (1, "Pro Analytics", 999),
        (2, "Growth Toolkit", 1499),
        (3, "Premium Support", 799),
        (4, "Annual Pro Upgrade", 2499),
    ]

    connection.executemany(
        """
        INSERT INTO customers
        (id, name, email, total_orders, total_spend, last_order_days_ago)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        customers,
    )

    connection.executemany(
        """
        INSERT INTO products
        (id, name, price)
        VALUES (?, ?, ?)
        """,
        products,
    )

    now = datetime.now()

    orders = [
        (1, 1, 1, 999, now - timedelta(days=7)),
        (2, 1, 2, 1499, now - timedelta(days=25)),
        (3, 2, 1, 999, now - timedelta(days=12)),
        (4, 2, 3, 799, now - timedelta(days=40)),
        (5, 3, 1, 999, now - timedelta(days=4)),
        (6, 3, 2, 1499, now - timedelta(days=18)),
        (7, 3, 4, 2499, now - timedelta(days=60)),
        (8, 4, 1, 999, now - timedelta(days=35)),
        (9, 5, 1, 999, now - timedelta(days=9)),
        (10, 5, 3, 799, now - timedelta(days=30)),
        (11, 6, 2, 1499, now - timedelta(days=42)),
        (12, 7, 1, 999, now - timedelta(days=6)),
        (13, 7, 2, 1499, now - timedelta(days=20)),
        (14, 7, 4, 2499, now - timedelta(days=75)),
        (15, 8, 1, 999, now - timedelta(days=28)),
        (16, 9, 3, 799, now - timedelta(days=14)),
        (17, 10, 1, 999, now - timedelta(days=5)),
        
    ]

    connection.executemany(
        """
        INSERT INTO orders
        (id, customer_id, product_id, amount, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        [
            (
                order_id,
                customer_id,
                product_id,
                amount,
                created_at.isoformat(),
            )
            for order_id, customer_id, product_id, amount, created_at in orders
        ],
    )

    connection.commit()
    connection.close()

    print("Demo merchant data seeded successfully.")


if __name__ == "__main__":
    seed_database()