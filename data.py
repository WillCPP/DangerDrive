import csv

with open('accidentTEST.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    data = [row for row in csv_reader]
    print(data)

    newdata = [[row['STATE'],row['ST_CASE'], row['PERSONS'],row['LATITUDE'], row['LONGITUD'],row['FATALS'],] for row in data]

    print(newdata)
