# IMDb Movie Explorer

![IMDb Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0-red)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3.0-green)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.0.0-orange)](https://plotly.com/)

## Overview

IMDb Movie Explorer is an interactive web application that allows users to explore and analyze a dataset of IMDb movies from 2023. Built with Streamlit, this app provides various filtering options and dynamic visualizations to help users gain insights into movie data.

## Features

- **Filtering Options**: Filter movies by director, year, and actor using the sidebar controls.
- **Data Display**: View filtered movie data in a sortable and searchable table.
- **Interactive Visualizations**:
  - **Rating Distribution**: Histogram showing the distribution of movie ratings.
  - **Top Directors**: Pie chart highlighting the top 20 directors by the number of movies.
  - **Mean Rating per Director**: Pie chart displaying the top 20 directors with the highest average movie ratings.
  - **Mean Votes per Director**: Pie chart showcasing the directors with the highest average number of votes per movie.
  - **Top Actors**: Pie chart listing the top 20 actors by the number of movies they have appeared in.
  - **Movies by Year Distribution**: Histogram illustrating the distribution of movies released each year.
  - **Meta Score by IMDb Rating**: Scatter plot showing the relationship between IMDb ratings and Meta Scores.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- Pandas
- Plotly

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TheODDYSEY/IMDB-Movie-Project.git
    cd imdb-movie-explorer
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501`.
2. Use the sidebar to filter movies by director, year, or actor.
3. Explore the various interactive visualizations and data tables.

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)
![Screenshot 3](screenshots/screenshot3.png)

## Data Source

The movie data used in this project is sourced from IMDb and includes information on movies released in 2023.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- IMDb for providing the movie data.
- Streamlit, Pandas, and Plotly for their powerful data visualization tools.

---

Feel free to replace `yourusername` in the repository URL with your actual GitHub username and update the screenshots with actual images from your app. This README provides a comprehensive guide to your project, highlighting its features and usage.
