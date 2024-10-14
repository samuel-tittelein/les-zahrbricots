import csv

# Renvoie une liste de listes contenant les données du fichier CSV
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            next(reader)  # Skip le header de chaque colonne
            rows = []
            for row in reader:
                rows.append(row)
            return rows