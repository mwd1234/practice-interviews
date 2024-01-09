# Create a function to remove stop words from a given text using Python.

import nltk
from nltk.corpus import stopwords

def remove_stopwords(text):
    words = nltk.word_tokenize(text)
    
    # Get the list of English stopwords from NLTK
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords from the text and create a filtered list of words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a sentence
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

input_text = "NLTK is a great tool for natural language processing, which removes stop words effectively."

text_without_stopwords = remove_stopwords(input_text)
print(text_without_stopwords)
