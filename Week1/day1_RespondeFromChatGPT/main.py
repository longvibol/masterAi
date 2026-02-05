import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

def messageChate():

    message = "Hello, GPT! This is my first ever message to you! Hi!"
    messages = [{"role": "user", "content": message}]

    openai = OpenAI()

    response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)
    repon = response.choices[0].message.content
    print(repon)

ed = fetch_website_contents("https://edwarddonner.com")
# print(ed)

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."
system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

"""
The API from OpenAI expects to receive messages in a particular structure.
Many of the other APIs share this structure:

[
    {"role": "system", "content": "system message goes here"},
    {"role": "user", "content": "user message goes here"}
]

"""
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]


openai = OpenAI()

response = openai.chat.completions.create(model="gpt-4.1-nano", messages=messages)
chat = response.choices[0].message.content

# See how this function creates exactly the format above

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

messages_for(ed)

# And now: call the OpenAI API. You will get very familiar with this!

def summarize(url):
    website = fetch_website_contents(url)
    response = openai.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

summarize("https://edwarddonner.com")

# A function to display this nicely in the output, using markdown

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

display_summary("https://edwarddonner.com")

























