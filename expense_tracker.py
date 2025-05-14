import psycopg2


conn = psycopg2.connect(
    dbname="notes_db",   
    user="postgres",     
    password="root",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def add_expense():
    amount = input("Enter amount (₹): ")  
    category = input("Enter category (e.g., Food, Transport): ")  

    if not amount or not category:  
        print("Amount and category are required!")
        return

    try:
       
        cur.execute("INSERT INTO expenses (amount, category) VALUES (%s, %s)", (amount, category))
        conn.commit()  
        print("Expense added successfully!")
    except Exception as e:
        print("Error:", e)


def view_expenses():
    
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    if not rows: 
        print("No expenses found!")
        return
    print("\n--- Your Expenses ---")
    for row in rows:
        print(f"ID: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]}")
    print("\n--- End of List ---")


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()  
        elif choice == '2':
            view_expenses()  
        elif choice == '3':
            print("Goodbye!")
            break 
        else:
            print("Invalid choice. Please try again.")  


main()

cur.close()
conn.close()

