![SDAIA_Academy](https://user-images.githubusercontent.com/20911835/136685524-fda5c7dd-6f97-480b-bb69-4ae1ad02c460.jpeg)

# FIFA 22 Players Overall Rating Prediction By Using Linear Regression

Faisal Alasgah

Omran Fallatah

### Abstract

The goal of this project was to use linear regression to predict the overall rating of football players in FIFA 22. We worked with the data we scraped from <https://www.fifaindex.com/> , Leveraging TODO feature engineering? along with linear regression to achieve promising results for this problem.

### Design

This project originated from our passion for football and FIFA game. The data is provided by our web scrapper. We used the data from fifindex.com to build our model that'll be able to predict future players overall rating.

### Data

FIFA 22 dataset contains 18,000 players (data points) and we selected 40 features for each player. A few feature highlights include Height, Weight, Age, Wage, Preferred Foot, and Overall Rating.

### Algorithms

###### Data scraping
  We started by trying to scrape the data from the FIFA official website with no luck. We switched to FIFA Index website and we were able to scrape all of their database of 18,000 players. Also, we selected 45 features out of 50+ features.


###### Data manipulation and cleaning.

-   Dropped unnecessary columns.

-   Applied feature engineering to some columns.

-   Dropped all duplicates data points.

-   Dropped all rows containing null or NaN values.

###### Model Evaluation and Selection

The entire training dataset of 17,012 records after applying feature engineering and data cleaning. The dataset was split into 60/20/20 train, test and validate.

After modeling and applying regularization we found the following results:

| Algorithm | Training R^2  | Validation R^2 |
| ------------- | ------------- | ------------- |
| Linear Regression | 0.889  | 0.892  |
| Lasso | 0.892  | 0.891  | 
| Ridge | 0.889  | 0.892  |


### Tools

-   Numpy and Pandas for data cleaning and manipulation.
-   Seaborn for plotting.
-   Selenium for beb scrapping.
-   Google Chrome for web scrapping.
-   Scikit-learn for modeling.

### Communication

In addition to the slides and the visuals included in the presentation, we will submit our code and proposal.
