![SDAIA_Academy](https://user-images.githubusercontent.com/20911835/136685524-fda5c7dd-6f97-480b-bb69-4ae1ad02c460.jpeg)

# FIFA 22 Players Overall Rating Prediction By Using Linear Regression

Faisal Alasgah

Omran Fallatah

### Abstract

<!--TODO Rewrite all the document -->

The goal of this project was to use linear regression to predict the overall rating of football players in FIFA 22. We worked with the data we scraped from <https://www.fifaindex.com/> , Leveraging TODO feature engineering? along with linear regression to achieve promising results for this problem.

### Design

This project originated from our passion for football and FIFA game. The data is provided by our web scrapper. We used the data from fifindex.com to build our model that'll be able to predict future players overall rating.

### Data

FIFA 22 dataset contains 18,000 players (data points) and we selected 40 features for each player. A few feature highlights include Height, Weight, Age, Wage, Preferred Foot, and Overall Rating.

### Algorithms

###### Data scraping?

<!-- \#ask Faisal and edit -->

###### Data manipulation and cleaning.

-   Dropped unnecessary columns.

-   Applied feature engineering to some columns.

-   Dropped all duplicates data points.

-   Dropped all rows containing null or NaN values.
<!---  
#### Model Evaluation and Selection

TODO:

The entire training dataset of 17,012 records after applying feature engineering and data cleaning. The dataset was split into 80/20 train vs. test, and all scores reported below were calculated with 5-fold cross validation on the training portion only. Predictions on the 20% holdout were limited to the very end, so this split was only used and scores seen just once.

The official metric for DrivenData was classification rate (accuracy); however, class weights were included to improve performance against F1 score and provide a more useful real-world application where classification of the minority class (functional needs repair) would be essential.

Final random forest 5-fold CV scores: 99 features (7 numeric) with class weights

Accuracy 0.797
F1 0.791 micro, 0.679 macro
precision 0.792 micro, 0.722 macro
recall 0.797 micro, 0.658 macro
--->
### Tools

-   Numpy and Pandas for data cleaning and manipulation.
-   Seaborn for plotting.
-   Selenium for beb scrapping.
-   Google Chrome for web scrapping.
-   Scikit-learn for modeling.

### Communication

In addition to the slides and the visuals included in the presentation, we will submit our code and proposal.
