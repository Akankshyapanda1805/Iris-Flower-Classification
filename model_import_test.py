import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Test input
inputs = np.array([6.5, 3.2, 5.1, 2]).reshape(1, 4)

# Predict
output = model.predict(inputs)

# Print the prediction result
print("Predicted class:", output[0])
