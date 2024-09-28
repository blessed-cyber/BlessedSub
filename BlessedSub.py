import socket
import os
import socket
from colorama import init
from termcolor import cprint
import argparse

# Initialize colorama
init()

# Print the banner
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


# الدالة لاختبار النطاق الفرعي
def check_subdomain(subdomain):
    try:
        # محاولة الحصول على عنوان IP الخاص بالنطاق الفرعي
        socket.gethostbyname(subdomain)
        return True
    except socket.gaierror:
        return False

# الدالة لاستعراض النطاقات الفرعية المحتملة
def find_subdomains(domain, wordlist):
    found_subdomains = []
    for word in wordlist:
        subdomain = f"{word}.{domain}"
        if check_subdomain(subdomain):
            found_subdomains.append(subdomain)
    return found_subdomains

# دالة لقراءة الكلمات المفتاحية من ملف
def load_wordlist(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: The file {filepath} does not exist.")
        return []
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]

# أخذ اسم النطاق من المستخدم
domain = input("Enter the domain (e.g., example.com): ")

# أخذ مسار ملف الكلمات المفتاحية من المستخدم
wordlist_path = input("Enter the path to your wordlist file: ")

# تحميل الكلمات المفتاحية من الملف
wordlist = load_wordlist(wordlist_path)

# التأكد من أن قائمة الكلمات ليست فارغة
if not wordlist:
    print("No words loaded from the wordlist file. Exiting.")
else:
    # البحث عن النطاقات الفرعية
    print(f"Searching subdomains for {domain}...")
    subdomains = find_subdomains(domain, wordlist)

    # عرض النتائج
    if subdomains:
        print("Found subdomains:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")
