import sys
from phone_book import PhoneBook

def handle_list_all_entries(phonebook):
    listing_all = phonebook.list_all_entries()
    print(f"Directory:\n{listing_all}")

def handle_add_entry(phonebook):
    last_name = input("Enter Last Name: ")
    first_name = input("Enter First Name: ")
    phone_number = input("Enter Phone Number: ")
    town = input("Enter Town name: ")
    phonebook.add_entry([last_name,first_name,phone_number,town])

def handle_delete_entry(phonebook):
    key = input("enter key to delete: ") 
    deleted_entry = phonebook.delete_entry(key)
    print(f"Deleted: {deleted_entry}")

def handle_list_entries_sorted_by_last_name(phonebook):
    sorted_listing = phonebook.list_sorted_by_last_name()
    print(f"Directory:\n{sorted_listing}")

def handle_list_entries_sorted_by_first_name(phonebook):
    sorted_listing = phonebook.list_sorted_by_first_name()
    print(f"Directory:\n{sorted_listing}")

def handle_list_entries_by_first_name(phonebook):
    first_name = input("Enter first name: ")
    sorted_listing = phonebook.list_entries_by_first_name(first_name)
    print(f"By {first_name}:\n{sorted_listing}")

def handle_list_entries_by_last_name(phonebook):
    last_name = input("Enter last name: ")
    sorted_listing = phonebook.list_entries_by_last_name(last_name)
    print(f"By {last_name}:\n{sorted_listing}")

def handle_list_entries_by_city(phonebook):
    city_name = input("Enter city name: ")
    sorted_listing = phonebook.list_entries_by_city(city_name)
    print(f"By {city_name}:\n{sorted_listing}")

input_handler = {"1":handle_list_all_entries,
                 "2":handle_add_entry,
                 "3":handle_delete_entry,
                 "4":handle_list_entries_sorted_by_last_name,
                 "5":handle_list_entries_sorted_by_first_name,
                 "6":handle_list_entries_by_first_name,
                 "7":handle_list_entries_by_last_name,
                 "8":handle_list_entries_by_city}

def phone_book_help():
    print("1 to list all entries")
    print("2 to add entry")
    print("3 to delete entry")
    print("4 to list entries sorted by last name")
    print("5 to list entries sorted by first name")
    print("6 to list entries by first name")
    print("7 to list entries by last name")
    print("8 to list entries by city")
    print("q to exit")

def main():

    _phone_book = PhoneBook()
    print("Phone Book is Open")

    phone_book_help()
    for line in sys.stdin:
        if (line.rstrip() == '1'):
            input_handler['1'](_phone_book)
        elif (line.rstrip() == '2'):
            input_handler['2'](_phone_book)
        elif (line.rstrip() == '3'):
            input_handler['3'](_phone_book)
        elif (line.rstrip() == '4'):
            input_handler['4'](_phone_book)
        elif (line.rstrip() == '5'):
            input_handler['5'](_phone_book)
        elif (line.rstrip() == '6'):
            input_handler['6'](_phone_book)
        elif (line.rstrip() == '7'):
            input_handler['7'](_phone_book)
        elif (line.rstrip() == '8'):
            input_handler['8'](_phone_book)
        elif (line.rstrip() == 'q') :
            break
        else:
            print("Unknown input")
        phone_book_help()       

if __name__ == "__main__":
    main()

