from data_collection import get_user_data
from raw_data import read_data
from group_data import group_data, draw_histogram
from statistics_module import compute_statistics

def main():
    menu = """***** Grouped Data Application *****\n"""
    menu += "Menu\n"
    menu += "1- Enter Data and Save in CSV\n"
    menu += "2- Show Statistics\n"
    menu += "3- Draw Histogram\n"
    menu += "4- Exit\n"
    menu += "Enter your Choice (1..4): "

    while True:
        choice = input(menu).strip()
        
        if choice == '1':
            print("\nEnter data and Save in CSV file.\n")
            get_user_data()
        
        elif choice == '2':
            print("\n --- Show the Statistics here---\n")
            data = read_data()
            if data:
                class_width = float(input("Enter class width: "))
                grouped_df, frequency, midpoints = group_data(data, class_width)
                stats_df = compute_statistics(data, grouped_df, frequency, midpoints)
                print(stats_df)
                stats_df.to_csv("statistics.csv", index=False)
                print("✅ Statistics saved to statistics.csv")
        
        elif choice == '3':
            print("\n --- Draw Histogram here---\n")  
            data = read_data()
            if data:
                class_width = float(input("Enter class width: "))
                grouped_df, _, _ = group_data(data, class_width)
                draw_histogram(grouped_df, class_width)
        
        elif choice == '4':
            print("\nExiting .....\n")
            break
        else:
            print("\nInvalid input, Try again.\n")

if __name__ == "__main__":
    main()