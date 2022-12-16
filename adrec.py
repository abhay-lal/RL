from matplotlib import pyplot as plt
import seaborn as sns
import scipy.stats as stats
import numpy as np

n_bandits = 4 # number of arms
p_bandits = [0.45, 0.50, 0.60, 0.70] # assumed probabilities of success for each arm

# define a function to pull an arm
def pull(chose_bandit): # iter is the index of the arm to pull
    if np.random.rand() < p_bandits[chose_bandit]:
        return 1
    else:
        return 0
# The number of trials and wins will represent the priority for each bandit with the help of beta distribuition

trials = [0] * n_bandits # number of trials for each arm
wins = [0] * n_bandits # number of wins for each arm

# Run trials for n steps while initializing it with 1
n = 1 
# define plots 
plots = [1,2,3,4,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000,1000000]

def plot(prior, step ,ax):
    plot_x = np.linspace(0.001,0.999,100)
    for prior in priors:
        plot_y = prior.pdf(plot_x)
        p = ax.plot(plot_x, y)
        ax.fill_between(plot_x, plot_y,0, alpha=0.2)
    ax.set_xlim([0,1])
    ax.set_ylim(bottom=0)
    ax.set_title(f'Prior at each step {step:d}')

for i in range(1,n+1):
    ## Define prior based on current observations
    bandits_prior = [ stats.beta(a=t+w, b=1+t-w ) for t,w in zip(trials,wins) ] # a is the number of successes and b is the number of failures


    ## plot prior 
    for step in plots:
        plot(bandits_prior,step,next(axs))
        
    theta_samples = [ d.rvs(1) for d in bandits_prior ] # sample from each prior
    chose_bandit = np.argmax(theta_samples) # choose the arm with the highest sample

    # choose a bandit using greedy strategy
    chose_bandit = np.argmax(theta_samples) 

    # pull the arm
    result = pull(chose_bandit)

    # update the number of trials and wins
    trials[chose_bandit] += 1
    wins[chose_bandit] += reward

plt.tight_layout()
plt.show()