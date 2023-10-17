from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import utils
    

class AB_experiment():
    """
    A/B Experiment for conversions.
    """
    def __init__(self, all_ctrl, target_ctrl,
                all_test, target_test,
                name = " Experiment n. ") -> None:
        
        #This is the known data
        self.all_ctrl, self.target_ctrl = all_ctrl, target_ctrl 
        self.all_test, self.target_test = all_test, target_test
        
        self.run()                              # lift, probability
        
        self.history = []                       # add history about experiments
        self.name = name 
           
    def calculate_posterior(self):
        a_C, b_C = self.target_ctrl+1, self.all_ctrl-self.target_ctrl+1
        self.beta_C = beta(a_C, b_C)

        # test beta 
        a_T, b_T = self.target_test+1, self.all_test-self.target_test+1
        self.beta_T = beta(a_T, b_T)
      
    
    def run(self):
        self.calculate_posterior()               # get self.beta_C self.beta_T
        
        self.lift = self.calculate_uplift()                     # calculate uplift
        self.probability = self.calculate_probab_criterion()    # calculate proba
       
    
    def calculate_uplift(self):
        #calculating the lift
        return (self.beta_T.mean()-self.beta_C.mean())/self.beta_C.mean()
    
    
    def calculate_probab_criterion(self):
        #calculating the probability for Test to be better than Control
        prob=utils.calc_prob_between(self.beta_T, self.beta_C)
        return prob 
    
    
    def plot_distrib(self, startend=[-0.002, 0.006]):
        '''this function plots the Beta distribution'''
        
        x=np.linspace(startend[0], startend[1], 100)
        for f, name in zip([self.beta_C, self.beta_T], ['Control', 'Test']):
            
            #this for calculate the value for the PDF at the specified x-points
            y = f.pdf(x)      
            
            y_mode = utils.calc_beta_mode(f.args[0], f.args[1])
            
            # the variance of the Beta distribution
            y_var = f.var()  
           
            plt.plot(x,y, label=f"{name} sample")
            print(f"{name} sample, conversion rate: {y_mode:0.1E}, pm: {y_var:0.1E}")
            plt.yticks([])
            
        plt.legend()
        plt.title(f'Plot pdf {self.name}')
        plt.show()
        
    
    def __str__(self):
        
        s = f"""
            Result {self.name}:

            Test option lift Conversion Rates by {self.lift}
            with {self.probability*100:2.1f}% probability;
            ================================================
            """
        return s
    
        
    def __add__(self, other):
        all_ctrl = self.all_ctrl + other.all_ctrl
        all_test = self.all_test + other.all_test
        
        target_ctrl = self.target_ctrl + other.target_ctrl
        target_test = self.target_test + other.target_test
        
        return AB_experiment(all_ctrl, target_ctrl, all_test, target_test)


class Data_sample():
    def __init__(self, all, target) -> None:   
        self.all = all
        self.target = target