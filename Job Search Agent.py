import anthropic
from colorama import Fore, Style, init
from dotenv import load_dotenv
import os
load_dotenv()
init()


client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) 

print(f"{Fore.GREEN}Welcome to the AI Job Search Agent!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}I'll search za web and find the top 10 job openings for you!\n")

while True:     # begin za loop
    job_title = input(f"{Fore.CYAN}Enter a job title to search; type 'quit' to exit: {Style.RESET_ALL}").strip()
    # prompt to enter job title

    if job_title.lower() == "quit":     # exits if 'quit' is entered
        print(f"{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
        break


    print(f"\n{Fore.CYAN}Work type:{Style.RESET_ALL}")
    print("1. Remote\n2. Hybrid\n3. On-site\n4. Any") # lists work type the user wants to see

    work_type = input(f"{Fore.CYAN}Choose (1-4): {Style.RESET_ALL}").strip() # prompt for work type choice
    work_type_map = {"1": "Remote", "2": "Hybrid", "3": "On-site", "4": "Any"} # dictionary; translates number into word-oh
    work_type = work_type_map.get(work_type, "Any") # defaults invalid keys to 'any'

    print(f"\n{Fore.CYAN}Experience level:{Style.RESET_ALL}")
    print("0. Internship\n1. Entry Level\n2. Mid Level\n3. Senior level\n4. Any")

    level = input(f"{Fore.CYAN}Choose (0-4): {Style.RESET_ALL}").strip() # prompts for skill level choice
    level_map = {"0": "Internship", "1": "Entry Level", "2": "Mid Level", "3": "Senior Level", "4": "Any"} # dictionary; translates number into word-oh
    level = level_map.get(level, "Any")  # translates number into word

    # prompt for country choice
    country = input(f"\n{Fore.CYAN}Enter country (e.g. United States (US), Japan, Any): {Style.RESET_ALL}").strip()
    

    # prompt for claude
    search_prompt = f"""
    You are a job search agent. Search the web and find the top 10 job openings for the following:

    - Job Title: {job_title}
    - Work Type: {work_type}
    - Experience Level: {level}
    - Country: {country}

    STRICT RULES:
    - Return EXACTLY 10 jobs, no exceptions
    - Do NOT explain limitations or why you can't find links
    - If a direct link isn't available, use the job board search URL
    - If salary isn't listed, write "Not Listed"
    - Never suggest the user search manually

    Format each job EXACTLY like this:
    ---
    Job #[number]
    Title: [title]
    Company: [company]
    Location: [location]
    Work Type: [work type]
    Level: [level]
    Salary: [salary or Not Listed]
    Link: [url]
    ---
    """

    print(f"\n{Fore.YELLOW}🔍 Searching for jobs... please wait... \n{Style.RESET_ALL}")

    try:
        response = client.messages.create(
        model="claude-sonnet-4-5", # claude model to use
        max_tokens=2000, # limits response length
        tools=[{"type": "web_search_20250305", "name": "web_search"}], # let's claude search za web
        messages=[{"role": "user", "content": search_prompt}] # search prompt is the message
        ) # sends request to claude

        reply = ""  #tis an empty reply
        for block in response.content: # loops through each response
            if hasattr(block, "text"):  # checks for text
                reply += block.text     # adds the text to za reply 

        print(f"{Fore.GREEN}✅ Top 10 Job Results for '{job_title}':{Style.RESET_ALL}\n")
        print(f"{Fore.MAGENTA}{reply}{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}Search complete! Ready for another one!{Style.RESET_ALL}\n")

    except anthropic.RateLimitError:
        print(f"{Fore.RED}⏳ Rate limit hit. Please wait 60 seconds and try again. {Style.RESET_ALL}")

    except anthropic.BadRequestError:
        print(f"{Fore.RED}❌ Search failed. Please try again.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}❌ Unexpected error: {e}{Style.RESET_ALL}")


