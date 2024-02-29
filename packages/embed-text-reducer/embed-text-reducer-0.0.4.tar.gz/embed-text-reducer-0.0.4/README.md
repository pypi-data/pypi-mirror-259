# EmbedTextReducer

TextReducer is a Python library for simplifying text content using advanced Natural Language Processing (NLP) techniques. It filters and summarizes text based on relevance to a given query, making it easier to extract meaningful information from large texts.

## Features

- Split text into sentences.
- Filter sentences based on token count.
- Compute cosine similarity between sentences and a given query.
- Summarize text by relevance to the query.

## Installation

Install TextReducer using pip:

```bash
pip install embed-text-reducer
```

## Usage
Here's a quick example to get you started:

```python
from embed_text_reducer import TextReducer

# Initialize the simplifier with default models
simplifier = TextReducer()

# Fit the text
text = "Your long text here. It will be split into sentences, filtered, and summarized."
simplifier.fit(text)

# Find relevant sentences to your query
query = "specific information"
summary, tokens = simplifier.find_relevant(query, max_tokens=100)

print("Summary:", summary)
print("Tokens used:", tokens)
```
