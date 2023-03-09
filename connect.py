import apikey
import datetime
import openai
import os

def main():

    def makeMessage(role, message):
        newmessage = {'role':role, 'content':message}
        return newmessage
    
    def makeTranscript(message_history):
        now = datetime.datetime.now()
        currentdate = now.strftime('%Y/%m/%d-%H:%M:%S')
        f = open('transcript.txt', 'a+', encoding='utf-8')
        f.write("\n" + currentdate + "\n")
        for message in message_history:
            role = message['role']
            content = message['content']
            f.write(role + ": " + content + "\n")
        f.close()
        
        return 0

    tokens = 0
    openai.api_key = apikey.KEY
    history = []
    startup_prompt = input("Startup prompt: ")
    history.append( makeMessage('system', startup_prompt) )
    run = True

    while run == True:
        userinput = input("User: ")
        newmessage = makeMessage('user', userinput)
        
        if userinput == 'bye':
            makeTranscript(history)
            run = False
            break
        elif userinput == 'RECALL:':
            for ndx in range(0,len(history)):
                print(str(ndx) + ": " + history[ndx]['role'] + " - " + history[ndx]['content'])
        else:
            history.append(newmessage)
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=history
                                                    )
            agent_response = response['choices'][0]['message']['content']
            agent_message = makeMessage('assistant', agent_response)
            history.append(agent_message)
            tokens += response['usage']['total_tokens']
            print("\nAgent: " + agent_response +"\n")
            print(str(tokens) + "/4096\n")
        

if __name__ == "__main__":
    main()
