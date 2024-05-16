import csv

# Path to file
pybank_csv = r"PyBank\Resources\budget_data.csv" 


# Opening file to then read it for the data within
with open(pybank_csv) as bank_data:
    read_data = csv.reader(bank_data)
    
    # Skip first row (header)
    header = next(read_data)
    
    # Variables to achieve the data goal
    first_row = next(read_data)
    months = 1
    profit = int(first_row[1])
    previous_net = int(first_row[1])
    net_change_list = []
    date = []

    # For loop to go through the dataset
    for row in read_data:
        months += 1
        profit += int(row[1])
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list += [net_change]
        date.append(row[0])
        greatest_increase = max(net_change_list)
        greatest_decrease = min(net_change_list)
        increase_date = date[net_change_list.index(greatest_increase)]
        decrease_date = date[net_change_list.index(greatest_decrease)]

    # Calculating the average through the net list items
    average_net = sum(net_change_list)/len(net_change_list)

# Printing out results formatted to the terminal
print("\nFinancial Analysis \n")
print("------------------------------------------- \n")
print(f"Total Months: {months} \n")      
print(f"Total: ${profit} \n")
print(f"Average Change = ${round(average_net,2)} \n")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase}) \n")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease}) \n")

# Finally creating a text file to write the results into
with open('financial analysis.txt', 'w') as text:
    text.write("Financial Analysis \n \n"),
    text.write("------------------------------------------- \n \n"),
    text.write(f"Total Months: {months} \n \n"),
    text.write(f"Total: ${profit} \n \n"),
    text.write(f"Average Change = ${round(average_net,2)} \n \n"),
    text.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase}) \n \n"),
    text.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")