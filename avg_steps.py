import csv

infile = open('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')

months = ['Janurary','Feburary','March','April','May','June','July','August','September','October','November','December']

