import socket
import os
import socket
from colorama import init
from termcolor import cprint
import argparse


init()


cprint("""
 ____  _                        _  _____       _     
|  _ \| |                      | |/ ____|     | |    
| |_) | | ___  ___ ___  ___  __| | (___  _   _| |__  
|  _ <| |/ _ \/ __/ __|/ _ \/ _` |\___ \| | | | '_ \ 
| |_) | |  __/\__ \__ \  __/ (_| |____) | |_| | |_) |
|____/|_|\___||___/___/\___|\__,_|_____/ \__,_|_.__/ 

Version 1.0
Developed by Team Blessed
""", "red")



def check_subdomain(subdomain):
    try:
      
        socket.gethostbyname(subdomain)
        return True
    except socket.gaierror:
        return False


def find_subdomains(domain, wordlist):
    found_subdomains = []
    for word in wordlist:
        subdomain = f"{word}.{domain}"
        if check_subdomain(subdomain):
            found_subdomains.append(subdomain)
    return found_subdomains


def load_wordlist(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: The file {filepath} does not exist.")
        return []
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]


domain = input("Enter the domain (e.g., example.com): ")

wordlist_path = input("Enter the path to your wordlist file: ")


wordlist = load_wordlist(wordlist_path)


if not wordlist:
    print("No words loaded from the wordlist file. Exiting.")
else:

    print(f"Searching subdomains for {domain}...")
    subdomains = find_subdomains(domain, wordlist)

   
    if subdomains:
        print("Found subdomains:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")
