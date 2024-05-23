import streamlit as st
import pandas as pd
import plotly.express as px

# Set page to wide mode
st.set_page_config(layout="wide")

# Load the movie data
data = pd.read_csv('imdb_movie_data_2023.csv')

# Streamlit UI
st.title('IMDb Movie Explorer')

# Sidebar for filtering options
director_options = data['Director'].unique().tolist()
year_options = sorted(data['Year'].unique().tolist())
actor_options = sorted(set(actor.strip() for actors in data['Cast'].dropna() for actor in actors.split(',')))

selected_director = st.sidebar.selectbox('Select a Director:', ['All'] + director_options)
selected_year = st.sidebar.selectbox('Select a Year:', ['All'] + year_options)
selected_actor = st.sidebar.selectbox('Select an Actor:', ['All'] + actor_options)
with st.sidebar.expander('About', expanded=True):
    st.write('''
        - Data: [IMDb Movie Data](https://www.kaggle.com/datasets/kianindeed/imdb-movie-dataset-dec-2023).
        - **Top Directors**: Directors with the most movies.
        - **Mean Rating per Director**: Average movie rating for directors.
        - **Top Actors**: Actors who have appeared in the most movies.
        - **Movies by Year Distribution**: Distribution of movies over the years.
    ''')
# Filter the DataFrame based on the selected director, year, and actor
filtered_data = data.copy()
if selected_director != 'All':
    filtered_data = filtered_data[filtered_data['Director'] == selected_director]
if selected_year != 'All':
    filtered_data = filtered_data[filtered_data['Year'] == selected_year]
if selected_actor != 'All':
    filtered_data = filtered_data[filtered_data['Cast'].apply(lambda x: selected_actor in x if pd.notnull(x) else False)]

# Display the filtered DataFrame
st.subheader(f'Movies Filtered by Director: {selected_director}, Year: {selected_year}, Actor: {selected_actor}')
st.dataframe(filtered_data)


# Interactive visualization with Plotly
fig = px.histogram(filtered_data, x='Rating', nbins=50, title=f'Rating Distribution for Filtered Movies')
st.plotly_chart(fig)

# Top Directors
top_directors = data['Director'].value_counts()[:20]
fig_bar = px.bar(top_directors, x=top_directors.index, y=top_directors.values, title='Top Directors')
fig_bar.update_layout(autosize=False, width=800, height=800, xaxis_title="Director", yaxis_title="Count", bargap=0.2)
st.plotly_chart(fig_bar)

# Mean Rating per Director
mean_rating_per_director = data.groupby('Director')['Rating'].mean().nlargest(20)
fig_pie = px.pie(mean_rating_per_director, names=mean_rating_per_director.index, values=mean_rating_per_director.values, title='Mean Rating per Director')
fig_pie.update_layout(autosize=False, width=800, height=800)
st.plotly_chart(fig_pie)

# Mean Votes per Director
mean_votes_per_director = data.groupby('Director')['Votes'].mean().nlargest(20)
fig_bar = px.bar(mean_votes_per_director, x=mean_votes_per_director.index, y=mean_votes_per_director.values, title='Mean Votes per Director')
fig_bar.update_layout(autosize=False, width=800, height=800, xaxis_title="Director", yaxis_title="Mean Votes", bargap=0.2)
st.plotly_chart(fig_bar)

# Top Actors
actors_dict = pd.Series([actor.strip() for actors in data['Cast'].dropna() for actor in actors.split(',')]).value_counts().head(20)
fig_bar = px.bar(actors_dict, x=actors_dict.index, y=actors_dict.values, title='Top Actors by Movie Count')
fig_bar.update_layout(autosize=False, width=800, height=800, xaxis_title="Actor", yaxis_title="Movie Count", bargap=0.2)
st.plotly_chart(fig_bar)

# Movies by Year Distribution
fig = px.histogram(data, x='Year', nbins=data['Year'].nunique(), title='Movies by Year Distribution')
st.plotly_chart(fig)

# Meta Score by IMDB Rating
fig = px.scatter(data, x='Rating', y='Meta Score', title='Meta Score by IMDB Rating')
st.plotly_chart(fig)