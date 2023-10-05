import os
import csv

print('os.getcwd', os.getcwd())
absolute_path = os.path.join(os.getcwd(), 'example.csv')

print('absolute_path', absolute_path)

open_file = open(absolute_path, 'w')
writer = csv.writer(open_file, delimiter=',')
open_file.close()