import anthropic
from colorama import Fore, Style, init
from dotenv import load_dotenv
import os
load_dotenv()
init()


print(f"{Fore.GREEN}Welcome to Document Q&A!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Tip: You can also drag n' drop your PDF file into the terminal to get its path!\n{Style.RESET_ALL}")
pdf_path = input(f"{Fore.CYAN}Enter za path to your PDF file: {Style.RESET_ALL}").strip(' \'"&') #takes out space, ', ", &
doc = pymupdf.open(pdf_path)
pdf_text = ""
for page in doc:
    pdf_text += page.get_text()

print(f"{Fore.GREEN}✅ PDF loaded! ({len(doc)} pages)\n{Style.RESET_ALL}") 

                                # api key goes here
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 

conversation = []


# how claude will behave
system_prompt = f"""You are a helpful assistant that answers questions based on the document below.
If the answer isn't in the document, you can search the web for additional information.

DOCUMENT:
{pdf_text}
"""

print(f"{Fore.CYAN} Ask me anything about your document! Type 'quit' to exit.\n{Style.RESET_ALL.strip()}")

while True:
    user_input = input(f"{Fore.CYAN}You: {Style.RESET_ALL}").strip()

    if not user_input:
        continue

    if user_input.lower() == "quit":
        print(f"{Fore.YELLOW}Goodbye! {Style.RESET_ALL }")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system=system_prompt,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=conversation
        )
        reply = ""
        for block in response.content:
            if hasattr(block, "text"):
                reply += block.text
    
    except anthropic.BadRequestError:
        reply = Fore.RED + "❌ Sorry, I can't help with that request." + Style.RESET_ALL
        conversation.pop()

    print(f"{Fore.YELLOW}Claude: {Fore.MAGENTA}{reply}{Style.RESET_ALL}\n")
    conversation.append({"role": "assistant", "content": reply})



