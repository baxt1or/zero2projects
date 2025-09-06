import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from datetime import datetime
from date_entry import get_date, get_amount, get_category, get_description, date_format


class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
    DATE_FORMAT = '%d-%m-%Y'
    
    @classmethod
    def initialize_csv(self):
        try:
            pd.read_csv(self.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['date', 'amount', 'category', 'description'])
            df.to_csv(self.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(self, date, amount, category, description):
        
        new_entry = {
            "date" : date, 
            "amount" : amount, 
            "category" : category, 
            "description" : description
        }

        with open(self.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.COLUMNS)
            writer.writerow(new_entry)
            print("Entry added successfully")
    
    @classmethod
    def get_transactions(self, start_date, end_date):
        df = pd.read_csv(self.CSV_FILE)

        df["date"] = pd.to_datetime(df["date"], errors='coerce', format=CSV.DATE_FORMAT)

        start_date = datetime.strptime(start_date, CSV.DATE_FORMAT)
        end_date = datetime.strptime(end_date, CSV.DATE_FORMAT)

        filtered_df = df[df["date"].between(start_date, end_date)]

        if filtered_df.empty:
            print("No transactions found in giver time interval")
        else:
            print(f'Transactions from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}')

            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.DATE_FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == 'Income']['amount'].sum()
            total_expenses = filtered_df[filtered_df["category"] == 'Expense']['amount'].sum()

            print('\nSummary:')
            print(f'Total Income: {total_income:.2f} UZS')
            print(f'Total Expenses: {total_expenses:.2f} UZS')
            print(f'Net Saving: {(total_income - total_expenses):.2f} UZS')
        
        return filtered_df




def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-year) or enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()

    CSV.add_entry(date, amount, category, description)


def plot_transactions(df : pd.DataFrame):
    
    df.set_index('date', inplace=True)

    income_df = df[df["category"] == 'Income'].resample('D').sum().reindex(df.index, fill_value=0)

    expenses_df = df[df["category"] == 'Expense'].resample('D').sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(15, 8))
    plt.plot(income_df.index, income_df["amount"], label='Income', color='g')
    plt.plot(expenses_df.index, expenses_df["amount"], label='Expenses', color='r')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title("Income vs. Expenses Over Time")
    plt.legend()
    plt.show()



def main():

    while True:
        print('\n 1. Add a new transaction')
        print('2. View transactions and summary within a date interval')
        print('3. Exit')

        choice = input('Enter your choice (1-3):')

        if choice == '1':
            add()
        elif choice == '2':
            start_date = get_date('Enter the start date (dd-mm-year): ')
            end_date = get_date('Enter the end date (dd-mm-year): ')
            df = CSV.get_transactions(start_date, end_date)

            if input('Do you want to see a plot? (y/n)').lower() == 'y':
                plot_transactions(df=df)
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter (1, 2 or 3).')


if __name__ == '__main__':
    main()