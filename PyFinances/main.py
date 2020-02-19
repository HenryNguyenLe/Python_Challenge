# Import modules for os and csv files
import os
import csv

# Build the path to the current csv file
fin_path = os.path.join('Resources','budget_data.csv')

# Create empty lists to store data
loss_gain_amount =[]
loss_gain_date = []
total_month = 0
gainloss_change = []

# Build the pipleline to the csv file and read data
with open(fin_path, newline='', encoding="utf-8") as csvfile:
          csvreader = csv.reader (csvfile,delimiter=',')
          csv_header = next(csvreader)
    
          
            
          #looping to store data
          for row_data in csvreader:
                
                # The total number of months included in the dataset 
                total_month += 1
                
                # add financial data and dates into pre-created empty lists 
                loss_gain_amount.append(int(row_data[0]))
                loss_gain_date.append(row_data[1])

                
                                
# The net total amount of "Profit/Losses" over the entire period
total_loss_gain = format(sum (loss_gain_amount),",")


# Create a new list of loss/ gain from one month to the next
for each_gainloss in range(1,len(loss_gain_amount)):
    gainloss_change.append(int(loss_gain_amount[each_gainloss]) - int(loss_gain_amount[each_gainloss - 1]))



# Calculate average change by total change / total amount of data points in the list
average_change = round(sum(gainloss_change) / len(gainloss_change), 2)


# The greatest increase in profits (date and amount) over the entire period
greatest_increase = max (gainloss_change)
greatest_increase_index = gainloss_change.index(greatest_increase)
greatest_increase_month = loss_gain_date[greatest_increase_index + 1]



# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min (gainloss_change)
greatest_decrease_index = gainloss_change.index(greatest_decrease)
greatest_decrease_month = loss_gain_date[greatest_decrease_index + 1]


# Print all results into Terminal
print('===========  BEGINNING OF THIS REPORT  ==========')
print('')
print('FINANCIAL ANALYSIS RESULTS')
print('')
print('-------------------------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total_loss_gain}')
print(f'Average  Change: ${format(average_change,",")}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${format(greatest_increase,",")})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${format(greatest_decrease,",")})')
print('')
print('============  THE END OF THIS REPORT  ===========')
      
      
# Export reports to a txt file
budget_report_path = os.path.join('Budget Report File.txt')
with open(budget_report_path, 'w', newline='', encoding="utf-8") as outputreport:
        outputreport.write('===========  BEGINNING OF THIS REPORT  ==========\n')
        outputreport.write('\n')
        outputreport.write('FINANCIAL ANALYSIS RESULTS\n')
        outputreport.write('')
        outputreport.write('-------------------------------------\n')
        outputreport.write(f'Total Months: {total_month}\n')
        outputreport.write(f'Total: ${total_loss_gain}\n')
        outputreport.write(f'Average  Change: ${format(average_change,",")}\n')
        outputreport.write(f'Greatest Increase in Profits: {greatest_increase_month} (${format(greatest_increase,",")})\n')
        outputreport.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${format(greatest_decrease,",")})\n')
        outputreport.write('\n')
        outputreport.write('============  THE END OF THIS REPORT  ===========')