from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('Rain', 'WetGrass'),
    ('Sprinkler', 'WetGrass')
])

# Step 2: Define CPDs
cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]  # No, Yes
)

cpd_sprinkler = TabularCPD(
    variable='Sprinkler',
    variable_card=2,
    values=[[0.6], [0.4]]  # Off, On
)

cpd_wetgrass = TabularCPD(
    variable='WetGrass',
    variable_card=2,
    values=[
        [0.99, 0.8, 0.9, 0.0],  # WetGrass = No
        [0.01, 0.2, 0.1, 1.0]   # WetGrass = Yes
    ],
    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2, 2]
)

# Step 3: Add CPDs to model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wetgrass)

# Step 4: Check model
print("Model is valid:", model.check_model())

# Step 5: Inference
inference = VariableElimination(model)

result = inference.query(variables=['WetGrass'], evidence={'Rain': 1})
print(result)

#Required Python Libraries
#pip install pgmpy numpy networkx scipy pandas
#python -m pip install --upgrade pip setuptools wheel
#pip install pgmpy


