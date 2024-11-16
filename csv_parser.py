import csv

# Renvoie une liste de listes contenant les données du fichier CSV
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = []
        next(reader)
        for row in reader:
            print(row) 
            rows.append(row)
        return rows
