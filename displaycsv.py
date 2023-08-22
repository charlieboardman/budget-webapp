import csv
from collections import deque

#Start the table
print("<table border='1' cellspacing='0' cellpadding='5'>")

with open('transactions.csv') as f:
    
    #Read the last 10 lines only
    last_lines = deque(f, maxlen=10)
    reader = csv.reader(last_lines)

    for row in reader:

        #Clean the number inputs, label the vendor
        vendor = row[0]
        pennies = float(row[1]) * 100
        dollars = "{:.2f}".format(pennies/100)
        #print(f"{vendor}, ${dollars}" + '<br>') #Use this for no table

        #Put the values into a table
        #Start a new table row
        print("<tr>")

        #Print each element in the row
        print(f"<td style='text-align:left;'>{vendor}</td>")
        print(f"<td style='text-align:right;'>${dollars}</td>")

        #End the table row
        print("</tr>")

    #End the table
    print("</table>")
        