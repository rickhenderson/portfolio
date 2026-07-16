# One of the first tutorials in the Anthropic course titled Building With the Claude API
# This was originally created in a Jupyter notebook.

# Load env variables. Use environment variables to keep secret tokens and API keys out of code repos like Github. Make sure to create a .gitignore.
from dotenv import load_dotenv
load_dotenv()

# Create an API client
from anthropic import Anthropic
client=Anthropic()
model = "claude-sonnet-4-5"
# model = "claude-haiku-4-5"  # With code completion in Visual Studio Code or other IDE, you'll be able to get the list of currently available models.

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

# Pass the current list of messages to Claude for a response.
def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
  
# If we want to have some semblance of memory, we need to maintain a list of every message we send 
# and receive, and provide that list with each follow up request.

# Create list of messages to start with
messages = []

# Add in the initial user question of "Define threat intelligence in one sentence."
add_user_message(messages, "Define threat intelligence in one sentence.")

# Pass the list into a "chat" to get an answer.
answer = chat(messages)

# Take the answer and add it as a message from the assistant to our list of messages.
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "Write another sentence.")

# Call chat again with the list of messages
answer = chat(messages)

# Display the result
answer
