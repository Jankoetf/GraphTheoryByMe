# GraphTheoryByMe
Graphs Graphs Graphs

# 1. Comparing DFS, BFS, A* on labyrinth problem
[data_analysis_preprocessing.ipnb](https://github.com/Jankoetf/GraphTheoryByMe/blob/main/labyrinth)
- Data analysis:
  
This is all about understanding features, what they represent. These are worthy of attention:
**league_id**: this is not just random generated id, but actually very important feature, it turns out that the bigger this league_id is the better that league_is - clubs in this league are better, we can see that by many corelations like:

<img src="Screeens/global.PNG" alt="Alt Text" width="312" height="256"> <img src="Screeens/payment.PNG" alt="Alt Text" width="312" height="256">

**club_id** again not just random generated number, but actually this id is generated in order, the bigger this id is that club created later

<img src="Screeens/club.PNG" alt="Alt Text" width="256" height="376">

- Preprocessing

I made two different preprocessing functions, one using both categorical features, one without them, you can see all functions in: 
[Copy_of_package.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Copy_of_Package.ipynb)

- Results simulation

Highest possible MAE is 7, if we generate predictions randomly it is oround 4.63, and if we generate for all predictions 7.5 we get 3.5 for MAE.


# 2. Ford Furkenson algorithm
[Feature_engeeniring.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Top_eleven_Feature_Ingineering.ipynb)
- Corelation analysis
<img src="Screeens/corelation.PNG" alt="Alt Text" width="428" height="256">

- Feature importance:

From many different models we get that playtime_last_28_days is most important feature.
<img src="Screeens/importance.PNG" alt="Alt Text" width="512" height="256">

- Feature Selection: 

After analysing corelations between features we get that two feature must be excluded from dataset, these are cohort_season because high corealtion with club_id(and club_id is required for submition), average_stars_top_14_players because of high corelation with average_stars_top_11_players(average_stars_top_11_players have higher importance)

- Feature Engeeniring

Because every feature have strong connection with league_id and predictions should have meaningfull order in the same league, feature engeeniring consist of averaging every feature by league average, and also droping old features except league_id and club_id. [Copy_of_package.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Copy_of_Package.ipynb)

# 3. Weighted graph, Djakstra algo
[Regression.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Top_eleven_regression.ipynb)
[Neural.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Top_eleven_neural.ipynb)

- Split

I did splitting into train, val, test set both with train_test_split function and manualy leaving grouped property of clubs in the same league, for easier post processing later. [Copy_of_package.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Copy_of_Package.ipynb)

- Hyperparameter tunning

Im using two step tunning aproach - hyperparameters tuning is splited into tuning of architecture parameters and tunning of regularization hyperparameters.

- Post-procesing

We see that every model predict conservatevly around 7.5 when it is unsertain.

<img src="Screeens/conservative.PNG" alt="Alt Text" width="312" height="256">

In order to transform predictions in meaningfull values I tried different post_processing functions, the simplest one has shown best performance(just rounding predictions in range 1, 14).

# 4. General Graphs
[Generating_results.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Top_eleven_generating_results.ipynb)
I choosed best neural network to generate results.

- **Resulting dataset**
[results.csv](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/league_rank_predictions.csv)

## **Thank you for exploring my project!** 
If you'd like to learn more about my background and qualifications, please visit my [LinkedIn profile](https://www.linkedin.com/in/jankomitrovic)
