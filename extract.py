"""
we are loading the spacy model and defining a function to extract entities and relevant information from the text. 
We are initializing variables to store the extracted information, such as the candidate's name, email, phone number, 
education details, work experience, and other skills.We are then iterating over the entities in the text and checking their labels. 
If the label is 'PERSON', we assume it is the candidate's name. If the label is 'PHONE', we assume it is the candidate's phone number. 
If the label is 'EMAIL', we assume it is the candidate's email address. If the label is 'ORG' and the text contains 'university', 
we assume it is the candidate's education details. If the label is 'ORG' and the text contains 'company', 
we assume it is the candidate's work experience. 
Finally, if the label is 'SKILL', we assume it is the candidate's skills.
We then return the extracted information as a dictionary. You can modify the code as per your requirements and use case.
"""

import spacy

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    # Apply the spacy model to the text
    doc = nlp(text)
    
    # Initialize variables to store the extracted information
    name = ''
    email = ''
    phone_number = ''
    education = []
    experience = []
    skills = []
    
    # Extract the entities and relevant information
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
        elif ent.label_ == 'PHONE':
            phone_number = ent.text
        elif ent.label_ == 'EMAIL':
            email = ent.text
        elif ent.label_ == 'ORG' and 'university' in ent.text.lower():
            education.append(ent.text)
        elif ent.label_ == 'ORG' and 'company' in ent.text.lower():
            experience.append(ent.text)
        elif ent.label_ == 'SKILL':
            skills.append(ent.text)
    
    # Return the extracted information
    return {
        'Name': name,
        'Email': email,
        'Phone Number': phone_number,
        'Education': education,
        'Experience': experience,
        'Skills': skills
    }
