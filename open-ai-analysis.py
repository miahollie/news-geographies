## import libraries
from openai import OpenAI
import csv

system_instructions = """
    Your task is to analyze the headlines of each article and determine whether the story is about a specific neighborhood in New York City or the city as a whole.
    Each text block should contain only one answer.
    
    The result should be "New York City" if the headline indicates that the story will be about all of the city.
    The result should be the name of the neighborhood if a specific neighborhood within New York City is included in the title.

    Do not provide any additional information.
"""
client = OpenAI()

def geography_analysis(text):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": system_instructions
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"{text}",
                            },
                        ],
                    }
                ],
            )
            return response.choices[0].message.content

with open("news-service-articles.csv", newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
        print(geography_analysis(row))
        

        




