import pandas as pd
from database import create_connection

def run_query(query):
    conn = create_connection()
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result

def get_movies_vs_tvshows():
    query = """
    SELECT type, COUNT(*) AS count
    FROM netflix
    GROUP BY type
    ORDER BY count DESC;
    """
    return run_query(query)

def get_top_release_year():
    query = """
    SELECT release_year, COUNT(*) AS number_of_titles
    FROM netflix
    GROUP BY release_year
    ORDER BY number_of_titles DESC
    LIMIT 10;
    """
    return run_query(query)

def get_ratings_distribution():
    query = """
    SELECT rating, COUNT(*) AS number_of_titles
    FROM netflix
    WHERE rating IS NOT NULL
    AND rating NOT LIKE '%min%'
    GROUP BY rating
    ORDER BY number_of_titles DESC;
    """
    return run_query(query)