import pickle

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Print model details
print("Model Type:", type(model))  # Should show DecisionTreeRegressor
print("\nModel Parameters:\n", model.get_params())  # Show model parameters
