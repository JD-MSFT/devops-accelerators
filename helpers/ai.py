import os
import requests
import json
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["AZURE_OPENAI_KEY"]
openai.api_base = os.environ[
    "AZURE_OPENAI_ENDPOINT"
]  # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = "azure"
openai.api_version = "2023-05-15"  # this may change in the future

deployment_name = "chat"  # This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
def ask(input):
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {
                "role": "system",
                "content": "You are an assistant who will generate a fun welcome message to a user that passes their name and job title.\nBe creative when coming up with the response based on job title.\nEnsure the response has a greeting and some kind of joke to remark based on the job title.\nAvoid using any product names in the response, instead use a general term for the product. An example would be replacing 'Googling' with 'looking up'.\nAvoid using any scenarios that could be seen as violent, like car crashes.",
            },
            {"role": "user", "content": "JD - Crane Operator"},
            {"role": "assistant", "content": "Hi JD, you're a Skywalker aren't you?"},
            {"role": "user", "content": "Mark - Chef"},
            {
                "role": "assistant",
                "content": "Hello Chef Mark, are you well today, or medium-well?",
            },
            {"role": "user", "content": input},
        ],
        max_tokens=100,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    text = response["choices"][0]["message"]["content"].strip()
    return text