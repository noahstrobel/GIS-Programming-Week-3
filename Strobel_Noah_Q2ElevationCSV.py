# Name:    Noah Strobel
# Class    GISC-450 Spring 2021

# Purpose: Displays longitude, latitude, and elevation data for the United States contained within a CSV file and
# omits longitude values less than -125 degrees and latitude values more than 49 degrees and less than 24.5 degrees.
# Additionally, it writes the coordinates to 4 decimal places and elevation to 1 to a new CSV file entitled
# "Strobel_Noah_SelectedCoTermPts.csv"

# Author:  Noah Strobel
# Created: 02/13/2021

################################################################
import csv


def main():
    print(f"\nThis program reads geographic data from a csv file, changes the data to omit longitude less than -125\
 degrees, latitude more than 49 degrees and less than 24.5 degrees.\nIt also writes the coordinates to 4 decimals and\
 elevation to 1 then creates and writes to a new file entitled 'Strobel_Noah_SelectedCoTermPts.csv'")

    file_name_in = r"C:\GISc450\PyRev3\elevationdata2.csv"
    file_name_out = r"C:\GISc450\PyRev3\Strobel_Noah_SelectedCoTermPts.csv"

    data_in = open(file_name_in, 'r')

    file_name_in = []
    longitude = []
    latitude = []
    elevation = []
    reader = csv.reader(data_in, delimiter=',')
    headers = next(reader)
    for line in reader:
        if float(line[1]) > -125 and float(line[0]) < 49 and float(line[0]) > 24.5:

            longitude.append(float(line[1]))
            latitude.append(float(line[0]))
            elevation.append(float(line[2]))
    records_out = len(longitude + latitude + elevation)
    print(f"\n\tRecords written out were {records_out}")

    data_attributes = len(longitude)
    print(f"\n{headers[1]:>10} {headers[0]:>10} {headers[2]:>10}")
    for line in range(data_attributes):
        print(f"{longitude[line]:>10.4f} {latitude[line]:>10} {elevation[line]:>10}")

    col = zip(longitude, latitude, elevation)
    with open(file_name_out, 'w', newline='') as csv_writer:
        writer = csv.writer(csv_writer)
        writer.writerow(headers)
        for row in col:
            writer.writerow(row)
        for line in col:
            writer.writerow(line)

    print(f"\nData written to {file_name_out}")


if __name__ == '__main__':
    main()
