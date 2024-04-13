import ktrain

# Load the saved predictor
predictor = ktrain.load_predictor("models")

# Input loop for making predictions
while True:
    user_input = input("Enter a text to predict emotion (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Make prediction
    prediction = predictor.predict(user_input)

    print("Predicted Emotion:", prediction)
