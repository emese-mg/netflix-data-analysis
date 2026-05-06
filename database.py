import sqlite3


def create_connection():
    conn = sqlite3.connect("netflix.db")
    return conn

def upload_to_database(df):
    conn = create_connection()

    df.to_sql(
        "netflix",
        conn,
        if_exists = "replace",
        index = False
    )

    conn.close()

    print("Data uploaded to database successfully.")