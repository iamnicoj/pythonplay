import os
import csv

def create_file_list_csv(directory, csv_filename):
    file_list = os.listdir(directory)
    file_list = sorted(file_list, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
   
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Row Number', 'File Name'])
        for i, file_name in enumerate(file_list, start=1):
            writer.writerow([i, file_name])

# Specify the directory path and the CSV file name
directory_path = '/Users/nicoj/Downloads/FinalNoMore'
csv_file_name = 'fotos-matri-SusanaNico.csv'

# Call the function
create_file_list_csv(directory_path, csv_file_name)

