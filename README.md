# UAM Simulator
2D agent-based simulation to evaluate some alternatives for low-altitude unmanned air traffic management.  
See *Ramee, C. and Mavris, D., "Development of a Framework to Compare Low-Altitude
Unmanned Air Traffic Management Systems", AIAA SciTech 2021, 2021.* for more details.
The code is distributed under the MIT license. Please cite the above paper if using this code.
## Installation
Clone the code and `python setup.py install`  
You will need an active Gurobi License to run the Local VO method.

## Running the code
The file example.py provides an example of how to run one simulation. Depending on the 
simulation type, agents density, and computer power one run can take anywhere from 5 
seconds to 10 hours.  
The results are saved to a JSON file containing a summary of the run settings, and metrics for each agent in the simulation.