"""
we are using regular expressions to remove unwanted characters and noise from the data. 
We are replacing multiple spaces with a single space, removing newlines, 
punctuation marks, and digits. We are then converting the data to lowercase to ensure consistency. 
Finally, we are removing stop words using the NLTK library. 
Stop words are words that occur frequently in the English language, 
such as 'a', 'the', 'in', etc., and do not add any value to the meaning of the text.
"""
import re

def preprocess_data(data):
    # Remove unwanted characters and noise from the data
    data = re.sub(r'\s+', ' ', data) # Replace multiple spaces with a single space
    data = re.sub(r'\n', '', data) # Remove newlines
    data = re.sub(r'[^\w\s]', '', data) # Remove punctuation marks
    data = re.sub(r'\d', '', data) # Remove digits
    
    # Convert the data to lowercase
    data = data.lower()
    
    # Remove stop words using NLTK
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    words = data.split()
    words = [word for word in words if word not in stop_words]
    data = ' '.join(words)
    
    return data