#!/usr/bin/python3
import csv

file = open('input.csv')
outputFile = open('output.csv', 'w', newline='')
writer = csv.writer(outputFile)
# now start writing the rows
reader = csv.reader(file)
for row in reader:
    name = row[0]
    surname = row[1]
    domain = row[2]

    writer.writerow(['%s%s@%s' % (name, surname, domain), name, surname, domain])
    writer.writerow(['%s@%s' % (name, domain), name, surname, domain])
    writer.writerow(['%s.%s@%s' % (name, surname, domain), name, surname, domain])
    writer.writerow(['%s%s@%s' % (name[:1], surname, domain),name, surname, domain])
    writer.writerow(['%s%s@%s' % (name, surname[:1], domain),name,surname, domain])
    writer.writerow(['%s%s@%s' % (name[:1], surname[:1], domain), name, surname, domain])
    writer.writerow(['%s%s@%s' % (surname, name, domain), name, surname, domain])
    writer.writerow(['%s%s@%s' % (surname, name[:1], domain), name, surname, domain])
    writer.writerow(['%s%s@%s' % (surname[:1], name, domain), name, surname, domain])
    writer.writerow(['%s%s@%s' % (surname[:1], name[:1], domain), name, surname, domain])
    # write the rows


outputFile.close()