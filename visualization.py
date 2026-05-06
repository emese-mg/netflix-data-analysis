import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



def plot_type_distribution(df):
    type_counts = df["type"].value_counts()

    type_counts.plot(
        kind = "bar",
        figsize = (8,5),
        color = ["#E50914", "#221F1F"]
    )

    plt.title("Netflix Movies vs Shows", fontsize = 16, fontweight = "bold")
    plt.xlabel("Type", fontsize = 12)
    plt.ylabel("Count", fontsize = 12)
    plt.xticks(rotation = 0)
    plt.grid(axis="y", linestyle = "--", alpha = 0.7)
    plt.tight_layout()

    plt.savefig(
        "outputs/type_distribution.png",
        dpi = 300
    )

    plt.show()

def plot_release_years(df):
    yearly_counts = df["release_year"].value_counts().sort_index()

    yearly_counts.plot(
        kind = "line",
        figsize = (12,6),
        color = "#E50914",
        linewidth = 2
    )

    plt.title(
        "Netflix Content Released by Year",
        fontsize = 16,
        fontweight = "bold"
    )

    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")
    plt.grid(linestyle = "--", alpha = 0.7)
    plt.tight_layout()

    plt.savefig(
        "outputs/release_years.png",
        dpi=300
    )

    plt.show()

def plot_top_countries(df):
    country_series = df["country"].dropna()
    countries = country_series.str.split(", ")
    exploded_countries = countries.explode()
    top_countries = exploded_countries.value_counts().head(10)

    top_countries.plot(
        kind = "barh",
        figsize = (10, 6),
        color = "#E50914"
    )

    plt.title(
        "Top 10 Countries by Netflix Content",
        fontsize = 16,
        fontweight = "bold"
    )

    plt.xlabel("Number of Titles")
    plt.ylabel("Country")
    plt.xticks(rotation = 0)
    plt.grid(axis="x", linestyle = "--", alpha = 0.7)
    plt.tight_layout()

    plt.savefig(
        "outputs/top_countries.png",
        dpi=300
    )

    plt.show()

def plot_top_genres(df):
    genre_series = df["listed_in"].dropna()
    genres = genre_series.str.split (", ")
    exploded_genres = genres.explode()
    top_genres = exploded_genres.value_counts().head(10)

    top_genres.plot(
        kind = "barh",
        figsize = (10,6),
        color = "#B20710"
    )

    plt.title(
        "Top 10 Netflix Genres",
        fontsize = 16,
        fontweight = "bold"
    )

    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")
    plt.grid(axis = "x", linestyle = "--", alpha = 0.7)
    plt.tight_layout()

    plt.savefig(
        "outputs/top_genres.png",
        dpi=300
    )

    plt.show()

def analyze_movie_durations(df):
    movies = df[df["type"] == "Movie"].copy()

    movies["duration_int"] = movies["duration"].str.replace(" min","", regex = False)

    movies["duration_int"] = pd.to_numeric(
        movies["duration_int"],
        errors = "coerce"
    )

    movies = movies.dropna(subset = ["duration_int"])

    print("\nMovie duration statistics:")
    print(movies["duration_int"].describe())

    plt.figure(figsize=(12,6))

    plt.hist(
        movies["duration_int"],
        bins = 30,
        color = "#E50914",
        edgecolor = "black",
        alpha = 0.8
    )

    plt.title(
        "Distribution of Movie Duration",
        fontsize = 18,
        fontweight = "bold",
        pad = 20
    )

    plt.xlabel("Duration (minutes)", fontsize = 12)
    plt.ylabel("Number of Movies", fontsize = 12)
    plt.grid(linestyle = "--", alpha = 0.4)
    plt.tight_layout()

    plt.savefig(
        "outputs/movie_durations.png",
        dpi=300
    )

    plt.show()

def plot_average_duration_by_genre(df):
    movies = df[df["type"] == "Movie"].copy()

    movies["duration_int"] = movies["duration"].str.replace(" min","",regex = False)

    movies["duration_int"] = pd.to_numeric(
        movies["duration_int"],
        errors = "coerce"
    )

    movies = movies.dropna(
        subset = ["duration_int", "listed_in"]
    )

    movies["genre"] = movies["listed_in"].str.split(", ")

    exploded_movies = movies.explode("genre")

    genre_duration = (
        exploded_movies.groupby("genre")["duration_int"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10,6))

    bars = plt.barh(
        genre_duration.index,
        genre_duration.values,
        color = "#B20710"
    )

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width + 1,
            bar.get_y() + bar.get_height()/2,
            f"{width:.1f}",
            va = "center"
        )

    plt.title(
        "Top 10 Genres by Average Movie Duration",
        fontsize = 16,
        fontweight = "bold"
    )

    plt.xlabel("Average Duration (min)")
    plt.ylabel("Genre")
    plt.grid(axis = "x", linestyle = "--", alpha = 0.7)
    plt.tight_layout()

    plt.savefig(
        "outputs/average_duration_by_genre.png",
        dpi=300
    )

    plt.show()

def plot_duration_vs_release_year(df):
    movies = df[df["type"] == "Movie"].copy()

    movies["duration_int"] = movies["duration"].str.replace(" min", "", regex = False)

    movies["duration_int"] = pd.to_numeric(
        movies["duration_int"],
        errors = "coerce"
    )

    movies = movies.dropna(subset = ["duration_int", "release_year"])
    movies = movies.sort_values("release_year")

    plt.figure(figsize=(12,6))

    plt.scatter(
        movies["release_year"],
        movies["duration_int"],
        alpha = 0.3,
        color = "#E50914",
        s = 15
    )

    z = np.polyfit(
        movies["release_year"],
        movies["duration_int"],
        1
    )

    p = np.poly1d(z)

    plt.plot(
        movies["release_year"],
        p(movies["release_year"]),
        color = "black",
        linewidth = 2
    )

    plt.title(
        "Movie Duration vs Release Year",
        fontsize = 16,
        fontweight = "bold"
    )

    plt.xlabel("Release Year")
    plt.ylabel("Duration (min)")
    plt.grid(linestyle = "--", alpha = 0.5)
    plt.tight_layout()

    plt.savefig(
        "outputs/duration_vs_release_year.png",
        dpi=300
    )

    plt.show()


