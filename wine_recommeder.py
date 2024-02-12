import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed wine data
wine_preprocessed = pd.read_csv('wine_preprocessed.csv')

# Create the Streamlit app
st.title('Wine Recommender')

# Define input widgets for brand, type, and rating
brand_options = ['None'] + list(wine_preprocessed['brand'].unique())
type_options = ['None'] + list(wine_preprocessed['wine_type'].unique())

# Brand selection dropdown
brand_input = st.selectbox('Select Brand:', options=brand_options)

# Type selection dropdown
type_input = st.selectbox('Select Wine Type:', options=type_options)

# Filter the data based on user inputs
if brand_input != 'None' and type_input != 'None':
    # Subheader for top five recommended wines
    st.subheader('Top Five Recommended Wines:')
    filtered_wines = wine_preprocessed[(wine_preprocessed['brand'] == brand_input) &
                                       (wine_preprocessed['wine_type'] == type_input)].head(10)
    for i, (index, wine) in enumerate(filtered_wines.iterrows(), start=1):
        st.subheader(f'Wine {i}: {wine["brand"]}')
        st.write(f"**Type:** {wine['wine_type']}")
        st.write(f"**Average Rating:** {wine['reviews.rating']:.2f}")
        st.write(f"**Review Text:** {wine['reviews.text']}")
        st.write(f"**Review Title:** {wine['reviews.title']}")
        st.write(f"**Review Username:** {wine['reviews.username']}")

    # Subheader for top five brands
    st.subheader('Top Five Brands:')
    top_five_brands = wine_preprocessed['brand'].value_counts().head()
    st.bar_chart(top_five_brands)

elif type_input != 'None':
    # Filter wines by selected type
    filtered_wines = wine_preprocessed[wine_preprocessed['wine_type'] == type_input]

    # Subheader for reviews of selected wine type
    st.subheader(f'Reviews for {type_input} Wine:')
    for i, (index, wine) in enumerate(filtered_wines.head(10).iterrows(), start=1):
        st.subheader(f'Review {i}:')
        st.write(f"**Type:** {wine['wine_type']}")
        st.write(f"**Rating:** {wine['reviews.rating']:.2f}")
        st.write(f"**Text:** {wine['reviews.text']}")
        st.write(f"**Title:** {wine['reviews.title']}")
        st.write(f"**Username:** {wine['reviews.username']}")

    # Subheader for recommended white and red wines
    st.subheader('Recommended White and Red Wines:')
    for wine_type, group in filtered_wines.groupby('wine_type'):
        recommended_wines = group['brand'].value_counts().head(5)
        st.write(f"**Recommended {wine_type.capitalize()} Wines:**")
        st.bar_chart(recommended_wines)

elif brand_input != 'None':
    st.subheader(f'Reviews for {brand_input}:')
    filtered_wines = wine_preprocessed[wine_preprocessed['brand'] == brand_input].head(10)
    for i, (index, wine) in enumerate(filtered_wines.iterrows(), start=1):
        st.subheader(f'Review {i}:')
        st.write(f"**Type:** {wine['wine_type']}")
        st.write(f"**Rating:** {wine['reviews.rating']:.2f}")
        st.write(f"**Text:** {wine['reviews.text']}")
        st.write(f"**Title:** {wine['reviews.title']}")
        st.write(f"**Username:** {wine['reviews.username']}")

    # Group data by brand, date added, and username and calculate average rating
    brand_date_user_ratings = filtered_wines.groupby(['brand', 'reviews.dateAdded', 'reviews.username'])['reviews.rating'].mean().reset_index()

    # Plot line graph
    plt.figure(figsize=(10, 6))
    for username, data in brand_date_user_ratings.groupby('reviews.username'):
        plt.plot(data['reviews.dateAdded'], data['reviews.rating'], marker='o', linestyle='-', label=username)
    plt.title('Wine Rating Trends by Brand and User')
    plt.xlabel('Date Added')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Username', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    st.pyplot(plt)

else:
    st.subheader('Top Five Brands:')
    top_five_brands = wine_preprocessed['brand'].value_counts().head()
    st.bar_chart(top_five_brands)
    st.write('No wines found matching the specified criteria.')
