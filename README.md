# UAM Simulator
2D agent-based simulation to evaluate some alternatives for low-altitude unmanned air traffic management.  
See *Ramee, C. and Mavris, D., "Development of a Framework to Compare Low-Altitude
Unmanned Air Traffic Management Systems", AIAA SciTech 2021, 2021.* for more details.  
The code is distributed under the MIT license. Please cite the above paper if using this code.
## Installation
First clone the code.  
`git clone https://github.com/colineRamee/UAM_simulator_scitech2021.git`  
Navigate to the new UAM_simulator_scitech2021 folder. 
 
### Using Anaconda  
To install the code dependencies in a new conda virtual environment:  
`conda env create - f uam_simulator_env.yml`  
`conda activate uam_simulator_env`  

### Using pip
When installing with pip, the gurobi library is called gurobipy. The setup.py file can be used to install dependecies by running: 
`python setup.py install`  

No matter what method is chosen, an active Gurobi license will be required to run the Local VO method. Other methods will work even without the Gurobi license.

## Running the code
The file example.py provides an example of how to run one simulation. Depending on the 
simulation type, agent density, and computational power, runtime can vary greatly. The visualization will crash if the simulation runs too slowly. It is advised to turn it off when running more than 50 agents. 
The results are saved to a JSON file containing a summary of the run settings, and metrics for each agent in the simulation.