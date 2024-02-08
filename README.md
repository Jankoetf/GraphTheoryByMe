# GraphTheoryByMe
Graphs Graphs Graphs

# 1. Ford Furkenson algorithm
[fordFurksenon.py](https://github.com/Jankoetf/GraphTheoryByMe/blob/main/fordFurksenon.py)

- Example

<p>
    <em>Small Regular Labyrinth</em> <img src="Pictures/ford Furksenon/s1.PNG" alt="Alt Text" width="228" height="126" alt> 
    <em>Labyrinth without Path</em> <img src="Pictures/Lavirint/no.PNG" alt="Alt Text" width="228" height="126" alt>
</p>
<p>
    <em>Big Labyrint</em> <img src="Pictures/Lavirint/big.PNG" alt="Alt Text" width="228" height="126" alt>
    <em>Small empty labyrinth</em> <img src="Pictures/Lavirint/empty.PNG" alt="Alt Text" width="228" height="126" alt>
</p>

# 2. Comparing DFS, BFS, A* on labyrinth problem
[Labyrinth.py](https://github.com/Jankoetf/GraphTheoryByMe/blob/main/lavirint.py)

-  Simulation Results:

| Labyrinth          | DFS | BFS | A*  |
|--------------------|-----|-----|-----|
| small regular      | 30  | 21  | 13 |
| small no path      | 18  | 9   |  8 |
| big many obstacles | 89  | 93  | 28 |
| small empty        | 895 | 154 |  9 |

- start is represented as 304, end with 707
-  1 means obstacle, 0 means no obstacle

<p>
    <em>Small Regular Labyrinth</em> <img src="Pictures/Lavirint/regular.PNG" alt="Alt Text" width="228" height="126" alt> 
    <em>Labyrinth without Path</em> <img src="Pictures/Lavirint/no.PNG" alt="Alt Text" width="228" height="126" alt>
</p>
<p>
    <em>Big Labyrint</em> <img src="Pictures/Lavirint/big.PNG" alt="Alt Text" width="228" height="126" alt>
    <em>Small empty labyrinth</em> <img src="Pictures/Lavirint/empty.PNG" alt="Alt Text" width="228" height="126" alt>
</p>



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
