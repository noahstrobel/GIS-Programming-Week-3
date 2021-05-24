# Name:    Noah Strobel
# Class    GISC-450 Spring 2021

# Purpose: Displays latitude, longitude, and elevation data for the United States contained within a CSV file.
# It also displays relevant information on the CSV file and writes a new CSV file entitled
# "Strobel_Noah_MyCoTermPts.csv."

# Author:  Noah Strobel
# Created: 02/11/2021

################################################################
import csv


def main():

    print("\n---This program reads latitude and longitude (both in decimal degrees)\
 and elevation data (in meters) for the United States and displays relevant information about its CSV file.")
    print("Additionally, it writes a new CSV file entitled 'Strobel_Noah_MyCoTermPts.csv'---")

    file_name_in = r"C:\GISc450\PyRev3\elevationdata2.csv"
    file_name_out = r"C:\GISc450\PyRev3\Strobel_Noah_MyCoTermPts.csv"

    data_in = open(file_name_in, 'r')

    longitude = []
    latitude = []
    elevation = []
    reader = csv.reader(data_in, delimiter=',')
    headers = next(reader)
    for line in reader:
        longitude.append(line[1])
        latitude.append((line[0]))
        elevation.append(line[2])

    records_read_in = len(longitude + latitude + elevation)
    print(f"\n\tTotal records read in were {records_read_in}. This includes all values in the elevation2.csv file")
    print(f"\tMaximum elevation is {max(elevation)} meters")
    print(f"\tMinimum elevation is {min(elevation)} meters")

    data_attributes = len(longitude)
    print(f"\n{headers[1]:>10} {headers[0]:>10} {headers[2]:>10}")
    for line in range(data_attributes):
        print(f"{longitude[line]:>10} {latitude[line]:>10} {elevation[line]:>10}")
        data_in.close()

    longitude = []
    latitude = []
    elevation = []

    with open(file_name_in, "r") as data_in:
        data_in.readline()
        for line in data_in:
            items = line.split(',')

            latitude.append(float(items[0]))
            longitude.append(float(items[1]))
            elevation.append(float(items[2]))

    with open(file_name_in, 'r') as data_in:
        reader = csv.reader(data_in, delimiter=",")
        headers = next(reader)
        for line in reader:
            longitude.append(line[0])
            latitude.append(line[1])
            elevation.append(line[2])

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
