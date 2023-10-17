# bayesian-a-b-testing-1  [notebooks](https://github.com/kodinkod/byes_a_b_tests/blob/main/bayesian-a-b-testing-1/pipline_1.ipynb)
p.s this is a project for learning. Supplemented

## 1. Generate test data;
<br>
<b>Control group</b> - Data about the system on which nothing has changed (the website page with the 'buy' button). number of observations, number of target events;
<br>
<b>Test group</b>  - Data about the same system on which we are testing new hypotheses (changed the color of the "buy" button).  number of observations, number of target events;


## 2. PDF's fot r test and control group
<p align="center">
<img width="596" align=center  src="img/aposterioir_pdf.png">
  
    λ - conversion, n - number of observations, c - number of target events, (a,b) - parameters of a priori probability.

</p>
<p align="center">
<img width="537"  src="img/aposterioir_pdf.png"> 
</p>

## 3. Calculating the lift

<p align="center">
<img width="383"  src="img/uplift.png">
</p>

## 4. Calculating probabiliti -  [code](https://github.com/kodinkod/byes_a_b_tests/blob/main/bayesian-a-b-testing-1/calc_prob.py)
<p align="center">
  
<img width="563" alt="Снимок экрана 2023-10-16 в 22 34 27" src="img/probability_criterion.png">
</p>

### Read 
 - [ Bayesian A/B Testing with Python: the easy guide ](https://towardsdatascience.com/bayesian-a-b-testing-with-python-the-easy-guide-d638f89e0b8a)


# bayesian-a-b-testing-2
