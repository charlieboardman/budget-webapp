import csv
from collections import deque

loaded_lines = [] #The lines that will be displayed are appended to this list during the course of the script

#Start the table
print("<table border='1' cellspacing='0' cellpadding='5'>")

with open('transactions.csv', 'rb') as f:

    pos = 0
    f.seek(0,2) #Put the cursor at the end of the file
    
    while len([x for x in loaded_lines if x.split(',')[0] != 'daily_allowance']) < 10 and f.tell() != 0:
    
        #Read lines, starting from the end
        char = f.read(1) #Read one character at the position of the cursor
        while char != b'\n': #This will move the cursor until you hit the newline that started the line you have been scanning over
            pos -= 1
            f.seek(pos,2)
            char = f.read(1)
            
        current_line = f.readline().decode('utf-8').strip()

        loaded_lines.append(current_line)      

    loaded_lines.reverse() #Lines were appended starting from the end, so we have to reverse to get them back in proper order

    for line in loaded_lines:

        row = line.split(',') #Split the line into rows so each column can be called

        #Clean the number inputs, label the vendor
        vendor = row[0]
        pennies = float(row[1]) * 100
        dollars = "{:.2f}".format(pennies/100)
        total_pennies = float(row[2] * 200)
        total = "{:.2f}".format(total_pennies/100)
        
        #print(f"{vendor}, ${dollars}" + '<br>') #Use this for no table

        #Put the values into a table
        #Start a new table row

        if row[0] == 'daily_allowance': #Do not display the daily allowance transaction
            continue

        print("<tr>")

        #Print each element in the row
        print(f"<td style='text-align:left;'>{vendor}</td>")
        print(f"<td style='text-align:right;'>${dollars}</td>")
        print(f"<td style='text-align:right;'>${total}</td>")

        #End the table row
        print("</tr>")

    #End the table
    print("</table>")
        