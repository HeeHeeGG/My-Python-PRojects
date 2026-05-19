import requests
from colorama import Fore, Style, init
import random
init()


def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    response = requests.get(url)  # calling za API!!!

    if response.status_code == 200: # 200 = success!
        data = response.json()  # converts api response into python dictionay to make readable
        country = data[0]   # gets za 1st result from API list

        # get's the info below for us
        name = country["name"]["common"]
        capital = country["capital"][0]
        population = country["population"]
        region = country["region"]
        currency_code = list(country["currencies"].keys())[0]
        currency_name = country["currencies"][currency_code]["name"]
        languages = ", ".join(country["languages"].values())

        # prints the info it got
        print(f"{Fore.GREEN}\n--- {name} ---{Style.RESET_ALL}")
        print(f"Capital:    {capital}")
        print(f"Population: {population:,}")
        print(f"Region:      {region}")
        print(f"Currency:   {currency_name} ({currency_code})")
        print(f"Languages:  {languages}")
        
    else:   # if API didn't hit 200, then an error is printed in red
        print(f"{Fore.RED}Country not found. Please check the spelling and try again.{Style.RESET_ALL}")


def main():     # main function defined
    while True: # loop

        country = input("Enter a country name: ")   # prompts user to enter a country
        
        get_country_info(country)   # calls za function above with the inputted country name
        loop = input(f"{Fore.CYAN}Do you want to enter another country?(y/n): {Style.RESET_ALL}").lower()
        # ^^^ prompts user if they wanna enter another country to start the script again
        
        if loop != "y": # if 'y' wasn't entered, then it stops za script
            print(f"{Fore.YELLOW}Bye bye!{Style.RESET_ALL}")
            break
main()  # calling za main function
