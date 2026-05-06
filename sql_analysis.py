

from queries import get_movies_vs_tvshows, get_top_release_year, get_ratings_distribution
import matplotlib.pyplot as plt


def show_sql_analysis():
    print("\n--- SQL Analysis Report---")

    print("\n1. Movies vs TV Shows:")
    print(get_movies_vs_tvshows())

    print("\n2. Top 10 years with the most netflix titles:")
    print(get_top_release_year())

    print("\n3. Rating distribution")
    print(get_ratings_distribution())

    plot_rating_distribution()

def plot_rating_distribution():
    ratings_df = get_ratings_distribution()

    ratings_df = ratings_df.sort_values(
        "number_of_titles",
        ascending = True
    )

    plt.figure(figsize=(12, 7))

    bars = plt.barh(
        ratings_df["rating"],
        ratings_df["number_of_titles"],
        color = "#E50914"
    )

    plt.title(
        "Netflix Rating Distribution",
        fontsize = 20,
        fontweight = "bold",
        pad = 20
    )

    plt.xlabel(
        "Number of Titles",
        fontsize = 12
    )

    plt.ylabel(
        "Rating",
        fontsize = 12
    )

    plt.grid(axis = "y", linestyle = "--", alpha = 0.7)

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width + 20,
            bar.get_y() + bar.get_height()/2,
            f"{int(width)}",
            va="center"
        )

    plt.tight_layout()

    plt.savefig(
        "outputs/rating_distribution.png",
        dpi=300
    )

    plt.show()