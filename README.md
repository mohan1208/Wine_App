## Introduction

The Wine Recommender is a web application designed to help users explore and discover wines based on their preferences. By leveraging a pre-processed dataset of wine reviews, the app allows users to filter wines by brand, type, and rating. It provides personalized recommendations, displaying the top five wines that match the user's selected criteria. Additionally, users can explore reviews for specific wine types or brands, along with trends in ratings over time. With its intuitive interface and data-driven recommendations, the Wine Recommender offers an engaging platform for wine enthusiasts to enhance their tasting experiences.

### A. Summary of the Analytic Application:

The analytic application I've built is a wine recommendation system designed to assist consumers in finding the right wine based on their preferences. The application utilizes two datasets: one containing wine reviews and another containing wine attributes. These datasets are joined together to create a comprehensive database of wines, including their brands, types, ratings, and other relevant information.

The application interface allows users to input their preferences, such as brand, type, and desired rating range. Based on these inputs, the system generates personalized wine recommendations. Users can explore detailed information about each recommended wine, including its average rating, reviews, and additional attributes. Furthermore, the application provides visualizations, such as histograms and boxplots, to help users understand the distribution of wine ratings and compare different wine types.

### B. How This Helps Solve the Issues of the Wine Company:

The wine recommendation system addresses several key issues faced by wine companies and consumers alike:
1. Enhanced Customer Experience: By providing personalized recommendations, the application enhances the overall customer experience. Consumers can easily discover wines that align with their preferences, leading to increased satisfaction and loyalty.
2. Improved Decision-Making: With access to detailed information and visualizations, consumers can make more informed decisions when selecting wines. They can explore reviews, ratings, and trends, empowering them to choose wines that suit their taste and budget.
3. Increased Sales and Customer Engagement: By offering tailored recommendations and valuable insights, the application encourages consumers to explore a wider range of wines. This can lead to increased sales for wine companies and greater engagement with their products.
4. Data-Driven Insights: The application provides wine companies with valuable data insights, such as consumer preferences and trends. This information can be used to optimize marketing strategies, product development, and inventory management.

### C. What does the product do:

This product build to be a wine recommender system built using Streamlit, a Python library for creating interactive web applications. The application allows users to explore wine data, filter wines based on brand, type, and rating, and view reviews and recommendations.
Here's an overview of its functionality:
1. Data Loading and Preprocessing: Initially, the program loads wine data from a CSV file (`combined_wine_data.csv`), preprocesses it by handling missing values, calculating statistics, and creating additional features like `wine_type` and `scraped_price`.
2. Interactive Streamlit App: The core of the product is a Streamlit web application titled "Wine Recommender." Users interact with the application through dropdown menus to select a brand, wine type, and optionally a rating.
3. Displaying Wine Reviews: The app displays wine reviews, including review text, title, rating, and username. Users can explore reviews for specific wine types or brands.
4. Recommendations: The application provides recommendations based on user-selected criteria. It can display top-rated wines, top-rated brands, or recommended wines of a specific type.
### D. Screenshots of how to use it.
Product Guide:
1.	Overview: Introduce the Wine Recommender app and its purpose. Explain that it helps users explore and find wines based on their preferences.

 <img width="368" alt="image" src="https://github.com/user-attachments/assets/21068b36-aad9-410d-9f4a-c184a9cd4048" />

Fig 1: Product Home Page.
2.	Input Options: 
•	Explain the input options available: brand, wine type, or both.
•	Provide details on the dropdown menus and their options.
  
  <img width="184" alt="image" src="https://github.com/user-attachments/assets/f6e21211-d0a1-4ebf-811a-fae74bd36223" />

  <img width="180" alt="image" src="https://github.com/user-attachments/assets/f4ff6ffa-5d53-457f-ab7f-ca6ff2091d47" />


Fig 3: Selecting All Parameter
3. Review Display:
•	Describe how reviews are displayed for selected wines or brands.
•	Emphasize the importance of reviews in decision-making.

 <img width="341" alt="image" src="https://github.com/user-attachments/assets/966ffc65-dc82-473d-a604-f9437f7ccd56" />

Fig 4: Default Page
E. Ways to Use:
If no specific criteria are selected, the app displays the top five brands present in the dataset and notifies users that no wines match the specified criteria.

 <img width="459" alt="image" src="https://github.com/user-attachments/assets/38be5940-9746-44af-9d59-07eb2cadabf7" />

Fig 5: Brand Selected Page
When brand is selected, it shows the reviews and also a graph when the review is given and by whom.

 <img width="291" alt="image" src="https://github.com/user-attachments/assets/75207c8a-23d5-492d-9dbc-2cfcf31b94d0" />

Fig 6: Brand Selected Page
There is slight difference when type only is selected you would be given reviews based on wine type and give recommendations of wines based on similarity in type. Limited the reviews to ten because some brands and types have more than then reviews.
 
<img width="380" alt="image" src="https://github.com/user-attachments/assets/69aff3d4-c16a-40b9-972f-1304f9055079" />

Fig 7: Type Selected Parameter
When both is given we will see the reviews with top recommendations using cosine similarity.

 <img width="452" alt="image" src="https://github.com/user-attachments/assets/5d59a8a1-557f-46f1-9696-ffbc9db1cf48" />

Fig 8: Both Parameters Selected.
 
Conclusion
In conclusion, the Wine Recommender app offers a comprehensive platform for wine enthusiasts to explore, discover, and evaluate various wines based on their preferences. Through intuitive filtering options and personalized recommendations, users can efficiently navigate through extensive wine selections, ensuring a tailored experience to suit individual tastes. Additionally, the app facilitates informed decision-making by presenting detailed reviews, ratings, and trend analyses. Whether users are seeking new favorites, planning events, or simply expanding their wine knowledge, the Wine Recommender app serves as a valuable tool, enhancing the wine exploration journey and enriching the overall wine appreciation experience.
References
1.	Deploy your app. Streamlit Docs. (n.d.). https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app 
2.	Git Add - fatal: adding files failed. (n.d.). Stack Overflow.
https://stackoverflow.com/questions/56675116/git-add-fatal-adding-files-failed
3.	GitHub: Let’s build from here. (n.d.). GitHub. https://github.com/


