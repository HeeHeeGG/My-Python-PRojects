import anthropic
from colorama import Fore, Back, Style, init
from dotenv import load_dotenv
import os
load_dotenv()
init()
                                 # api key goes here
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversation = []

print(Fore.GREEN + "Chat with Claude! Type 'quit' to exit.\n" + Style.RESET_ALL)

while True:
    user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL).strip()

    if not user_input:
        continue

    if user_input.lower() == "quit":
        print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
        break

    # adds the user's inputs into the conversation array
    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=conversation
        )
        reply = response.content[0].text
    
    except anthropic.BadRequestError as e:
        reply = Fore.RED + "Sorry, I can't help with that request" + Style.RESET_ALL # error message substitute
        conversation.pop() # removes failed message

    print(f"{Fore.YELLOW}Claude: {Fore.MAGENTA}{reply}{Style.RESET_ALL}") #fore color with f fucntion

    conversation.append({"role": "assistant", "content": reply})


