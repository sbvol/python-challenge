#Completing the initial imports
import os
import csv

#Creating all of my variables
month_year = []
revenue = []
row_current = []
rev_low_diff = 0
rev_high_diff = 0
monthly_rev_diff = 0
previous_rev = 0
total_rev_diff = 0
total_revenue = 0
number_of_months = 0
current_row = 0

#Building links to files and their locations
budget_data1 = os.path.join('../pythonstuff/budget_data_1.csv')
budget_data2 = os.path.join('../pythonstuff/budget_data_2.csv')

#Reading files
with open(budget_data1, newline="") as csvfile1:
    csvreader = csv.reader(csvfile1, delimiter=",")
    next(csvreader, None)
    
    for row in csvfile1:
        row_current = row.split(",")
        month_year.append(row_current[0])
        revenue.append(row_current[1])

with open(budget_data2, newline="") as csvfile2:
    csvreader = csv.reader(csvfile2, delimiter=",")
    next(csvreader, None)
    
    for row in csvfile2:
        row_current = row.split(",")
        month_year.append(row_current[0])
        revenue.append(row_current[1])

#Calculating total revenue
for dollar in revenue:
    total_revenue = total_revenue + int(dollar)

#Calculating number of months and changing variable type
number_of_months = len(month_year)
total_revenue = int(total_revenue)

#Looping to determine high and low monthly differentials
#Also determining total monthly differential
for rev in revenue:
    monthly_rev_diff = int(rev) - previous_rev
    if monthly_rev_diff > 0 and monthly_rev_diff > rev_high_diff:
        rev_high_diff = monthly_rev_diff
        rev_high_index = revenue.index(rev)
        rev_high_month_year = month_year[rev_high_index]
    
    if monthly_rev_diff < 0 and monthly_rev_diff < rev_low_diff:
        rev_low_diff = monthly_rev_diff
        rev_low_index = revenue.index(rev)
        rev_low_month_year = month_year[rev_low_index]
            
    previous_rev = int(rev)
    current_row = current_row + 1
    total_rev_diff = total_rev_diff + monthly_rev_diff

#Calculating average change per month over the entire dataset (from 2009 to 2016)    
avg_month_change_rev = total_rev_diff / number_of_months

#Formating the output
total_revenue = "$ %8.2f"% total_revenue
rev_high_diff = "$ %8.2f"% rev_high_diff
rev_low_diff = "$ %8.2f"% rev_low_diff
avg_month_change_rev = "$ %8.2f"% avg_month_change_rev

#Printing the output to the screen
print("Financial Analysis")
print("-------------------------------------")
print("Total Number of Months: " + str(number_of_months))
print("Total Revenue: "+ str(total_revenue))
print("Average Revenue Change: " + avg_month_change_rev)
print("Greatest Increase in Revenue: " + rev_high_month_year + " " +  rev_high_diff)
print("Greatest Decrease in Revenue: " + rev_low_month_year + " " +  rev_low_diff)

#Printing the output to the output folder
output_path = os.path.join('../pythonstuff/output', 'budget_analysis.csv')

with open(output_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["Total Number of Months: " + str(number_of_months)])
    csvwriter.writerow(["Total Revenue: "+ str(total_revenue)])
    csvwriter.writerow(["Average Revenue Change: " + avg_month_change_rev])
    csvwriter.writerow(["Greatest Increase in Revenue: " + rev_high_month_year + " " +  rev_high_diff])
    csvwriter.writerow(["Greatest Decrease in Revenue: " + rev_low_month_year + " " +  rev_low_diff])
