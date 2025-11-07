import json
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

# Load intents data
with open("intents.json") as file:
    data = json.load(file)

# Prepare text data
texts = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)

# Create and fit tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

# Save the tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("New tokenizer created and saved!")