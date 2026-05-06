from data_cleaning import load_data, clean_data
from database import upload_to_database
from sql_analysis import show_sql_analysis
from visualization import plot_type_distribution, plot_release_years, plot_top_countries, plot_top_genres, \
    analyze_movie_durations, plot_average_duration_by_genre, plot_duration_vs_release_year



def main():
    file_path = "netflix_titles.csv"

    df = load_data(file_path)
    df = clean_data(df)
    upload_to_database(df)

    plot_type_distribution(df)
    plot_release_years(df)
    plot_top_countries(df)
    plot_top_genres(df)
    analyze_movie_durations(df)
    plot_average_duration_by_genre(df)
    plot_duration_vs_release_year(df)

    show_sql_analysis()

if __name__ == '__main__':
    main()

