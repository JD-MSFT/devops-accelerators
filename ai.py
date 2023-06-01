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

default_prompt = "Generate a unique, fun, and clever greeting for an individual based on their name and job title. Don't just say something about having a good day.\n\nExample:\nJD - Software Engineer\nHi JD, you look like you've run into some bed bugs this morning!"

input = "Charles - Professional Golfer"

# Send a completion call to generate an answer
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=default_prompt + input,
    temperature=0.8,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.5,
    best_of=1,
    stop=None,
)

print(response)
