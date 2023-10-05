import csv

path = 'example.csv'
open_file = open(path, 'w')
writer = csv.writer(open_file, delimiter=',')
open_file.close()