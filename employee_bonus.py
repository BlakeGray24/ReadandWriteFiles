def main():
    import csv

    infile = ('EmployeePay.csv','r')

    csvfile = csv.reader(infile,delimiter=',')
    next(csvfile)

    #infile.readline()

    #infile.readline()
    #Repeating structure
    print('ID:')
    print('Full name:')
    print('Total salary:')

    input()

#def cal_total():
    #Calculate total here, location 4 & 5 in the list
