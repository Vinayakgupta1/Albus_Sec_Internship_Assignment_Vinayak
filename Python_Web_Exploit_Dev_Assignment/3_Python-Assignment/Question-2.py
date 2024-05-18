# Write a program to search for a specific pattern (e.g., email addresses or phone numbers) within a text file and extract them.

import re

def search_pattern(file_name, pattern):
  
    with open(file_name, 'r') as file:
        
        matches = re.findall(pattern, file.read())
        
    return matches

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

matches = search_pattern('vinayak1.txt', pattern)

for match in matches:
    print(match)