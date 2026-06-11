import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="sandbox_agent",
    user="postgres",
    password="postgres"
)

def get_total_users():
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM users"
    )

    count = cur.fetchone()[0]

    cur.close()

    return count

def get_all_messages():
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            user_id,
            prompt,
            response,
            input_tokens,
            cached_input_tokens,
            output_tokens,
            cost_usd,
            created_at
        FROM messages
        ORDER BY created_at DESC
    """
)

    rows = cur.fetchall()

    cur.close()

    return rows


def get_total_messages():
    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM messages"
    )

    count = cur.fetchone()[0]

    cur.close()

    return count

def save_message(
    user_id,
    prompt,
    response,
    input_tokens,
    cached_input_tokens,
    output_tokens,
    cost_usd
):
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO messages (
            user_id,
            prompt,
            response,
            input_tokens,
            cached_input_tokens,
            output_tokens,
            cost_usd
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            user_id,
            prompt,
            response,
            input_tokens,
            cached_input_tokens,
            output_tokens,
            cost_usd
        )
    )
    conn.commit()
    cur.close()
    
def get_user_history(user_id):
    cur = conn.cursor()

    cur.execute(
        """
        SELECT prompt, response
        FROM messages
        WHERE user_id = %s
        ORDER BY created_at
        LIMIT 10
        """,
        (user_id,)
    )

    rows = cur.fetchall()

    cur.close()

    return rows

def create_user_if_not_exists(user_id):

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users(user_id)
        VALUES(%s)
        ON CONFLICT (user_id)
        DO NOTHING
        """,
        (user_id,)
    )
    conn.commit()

    
    cur.close()