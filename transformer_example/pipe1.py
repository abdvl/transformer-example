from transformers import pipeline

# Load the pipeline
classifier = pipeline('sentiment-analysis')

# Classify a sentence
res = classifier('We are very happy to show you the 🤗 Transformers library.')

print(res)
