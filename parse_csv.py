import csv
# Opens cvs file and saves it to a value (cvs_file) and reads it through cvs_reader
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # Skips column header
#     next(csv_reader)

# Reads csv file as a Dictionary with key value pairs
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Opens NewNames file with a dictionary writer, names the fields, decides the delimiter
    with open('new_names.csv', 'w') as new_file:
        field_names = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')

        # Ensures csv files have header
        csv_writer.writeheader()

        # Prints lines in cvs file to console but deletes the email line
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)


# Prints each line as a dictionary
#     for line in csv_reader:
#         print(line)