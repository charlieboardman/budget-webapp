import sys

with open('total.txt', 'r') as total_file:
    total_str = total_file.read()

total = float(total_str)

delta = -float(sys.argv[1])
#delta = -25
new_total = total + delta

new_total_str = str(new_total)

with open('total.txt','w') as total_file:
    total_file.write(new_total_str)

with open('transactions.csv','a') as transactions:
    vendor = sys.argv[2]
    #vendor = 'walmart'
    line = '\n' + vendor + ',' + "{:.2f}".format(-delta) + ',' + new_total_str
    transactions.write(line)