from setuptools import setup

setup(
    name='uam_simulator',
    version='1.0',
    description='A tool to simulate different architectures for UAM traffic management',
    author='Coline Ramee',
    author_email='coline.ramee@gatech.edu',
    packages=['uam_simulator'],
    install_requires=['numpy', 'scikit-learn', 'gurobipy']
)
# If installing from source the package name is gurobipy, if installing with conda it's gurobi, but when importing it's still gurobipy
