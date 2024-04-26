# install Pint if necessary
import pandas as pd
from modsim import *

try:
    import pint
except ImportError:
    !pip install pint

# download modsim.py if necessary

# population = 10
un = table2.un / 1e9
census = table2.census / 1e9

//initial population stuff/original
# elapsed_time = t_end - t_0
//we want 2025?

# p_0 = census[t_0]
# p_end = census[t_end]

# total_growth = p_end - p_0
# annual_growth = total_growth / elapsed_time
annual_growth = 0.03
population = 8191988453


def snap(population):
    return population // 2

print(snap(population))

//20 years 
t_0 = 1
t_end = 20

p_0 = snap(population)
p_end = snap(population)

""" 
20+ years after it. Plot your model in the notebook. Provide a markdown cell with analysis of your results.
How long would it take the population to recover?
How might carrying capacity and maximum growth rate (as parameters) be affected by such a change?
"""
def recovering_post_snap():
    pass
    
"""
Now, imagine that someone "snaps" their fingers again, five (5) years after the original snap, 
and all the people who disappeared now suddenly reappear. 
What would happen to your model now? Plot your model in the notebook.
"""
def unsnappening():
    pass

"""
If population loss is attributable by death (starvation, disease, old age),
and the purpose of wiping out half of life was to reduce this “suffering”, what might be better methods of reducing suffering (vis-à-vis your model that is).
Expand the model in some way, and provide analysis.
"""
def alternate_realities():
    pass
    
def show_values(t0,t_end,p_0,annual_growth):
    system = System(t_0=t_0, t_end=t_end, p_0=p_0, annual_growth=annual_growth)
    show(system)
