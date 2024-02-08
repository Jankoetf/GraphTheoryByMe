# GraphTheoryByMe
Graphs Graphs Graphs

# 1. Ford Furkenson algorithm
[fordFurksenon.py](https://github.com/Jankoetf/GraphTheoryByMe/blob/main/fordFurksenon.py)

**Example: Jobs and workers**
- One worker can do at max one job
- Every job can have at max one worker doing it
- What is a maximum number of workers that can get a job?
<p>
    <img src="Pictures/Ford%20Furkenson/s1.PNG" alt="Alt Text" width="428" height="286" alt> 
</p>

- First Iteration
<p>
    <img src="Pictures/Ford%20Furkenson/s2.PNG" alt="Alt Text" width="428" height="286" alt> 
    <img src="Pictures/Ford%20Furkenson/s3.PNG" alt="Alt Text" width="428" height="286" alt> 
</p>

- Second Iteration
<p>
    <img src="Pictures/Ford%20Furkenson/s4.PNG" alt="Alt Text" width="428" height="286" alt> 
    <img src="Pictures/Ford%20Furkenson/s5.PNG" alt="Alt Text" width="428" height="286" alt> 
</p>
On this specific example we get that maximum 2 workers can get a job.


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
[Labyrinth.py](https://github.com/Jankoetf/GraphTheoryByMe/blob/main/lavirint.py)
<p>
    <em> Weighted Graph </em> <img src="Pictures/Lavirint/no.PNG" alt="Alt Text" width="228" height="126" alt>
</p>


# 4. General Graphs
[Generating_results.ipnb](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/Top_eleven_generating_results.ipynb)
I choosed best neural network to generate results.

- **Resulting dataset**
[results.csv](https://github.com/Jankoetf/Nordeus_data_science_challenge/blob/main/league_rank_predictions.csv)

## **Thank you for exploring my project!** 
If you'd like to learn more about my background and qualifications, please visit my [LinkedIn profile](https://www.linkedin.com/in/jankomitrovic)
