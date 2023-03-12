"""
In this file, we will define the parse_resume function that will parse the resume using the trained NLP model
we are defining the parse_resume function that takes a resume as input and returns the parsed data. 
We are using the spacy library to extract the entities and relevant information from the parsed data.
"""
import spacy

def parse_resume(resume):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(resume)

    # Extract the entities and relevant information from the parsed data
    name = ''
    email = ''
    phone = ''
    education = []
    experience = []
    skills = []
    # Your code to extract entities and relevant information goes here

    parsed_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'education': education,
        'experience': experience,
        'skills': skills
    }

    return parsed_data
