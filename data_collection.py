import pandas as pd

def get_user_data():
    print("Enter your continuous numerical data separated by commas (e.g., 12, 34.5, 22):")
    user_input = input("→ ").strip()
    try:
        values = [float(x) for x in user_input.split(",") if x]
        df = pd.DataFrame(values, columns=["Value"])
        df.to_csv("raw_data.csv", index=False)
        print("✅ Data saved to raw_data.csv")
    except ValueError:
        print("❌ Invalid input. Please enter numbers only, separated by commas.")