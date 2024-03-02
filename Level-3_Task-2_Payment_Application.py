def process_payment(amount):
    print(f"Processing payment of ${amount}...")
    print("Payment successful!")

def main():
    try:
        amount = float(input("Enter payment amount: $"))
        if amount <= 0:
            raise ValueError("Amount must be a positive number")
        
        process_payment(amount)
    except ValueError as e:
        print(f"Error: {e}")
        print("Payment failed.")

if __name__ == "__main__":
    main()
