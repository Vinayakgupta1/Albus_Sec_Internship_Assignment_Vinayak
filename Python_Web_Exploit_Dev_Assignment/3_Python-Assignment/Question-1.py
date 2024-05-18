# Write a program to read data from a CSV file and perform basic data cleaning operations like removing duplicates or handling missing values.


import csv

def read_csv_file(file_name):
    
    with open(file_name, 'r') as csvfile:
       
        reader = csv.reader(csvfile)
        
        header = next(reader)
        
        data = []
        for row in reader:
            data.append(row)
            
    return header, data

def remove_duplicates(data):

    unique_data = []
    for row in data:
        if row not in unique_data:
            unique_data.append(row)
            
    return unique_data

def handle_missing_values(data):
   
    default_value = 'N/A'
    for row in data:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = default_value
                
    return data


header, data = read_csv_file('vinayak.csv')

data = remove_duplicates(data)

data = handle_missing_values(data)

for row in data:
    print(row)