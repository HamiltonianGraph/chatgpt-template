# ChatGPT Template #

A basic Python template for CLI interaction with OpenAI's "gpt-3.5-turbo" model. This program works from your terminal or command line interface. Feel free to use as a base for your own applications.

Built for Python 3.10

### Requirements: ###
- an OpenAI API key
- openai Python module
- apikey (included with this repo, it's just a file to put your OpenAI API key into)
- an empty .txt file called "transcript.txt" - this is where the script appends the record of your chats)

### Setup: ###
1) Download the files

2) Insert your API key into the KEY variable in the apikey.py 

3) Run the chatgpt_connect.py script

4) Enter a setup prompt for the system (this sets the "system" variable in the message, giving overall guidance to the model)

5) Converse with the model user when prompted.
  
  To see your previous conversation history, type "RECALL:"
  
  To leave the conversation, type "bye" - this will trigger the script to output your chat history to the transcript.txt file
  



