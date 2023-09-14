import os
import datetime
import qrcode
import requests
import math
import platform
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_date_time():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now}")

def create_text_file():
    file_name = input("Enter the file name: ")
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created successfully!")

def generate_qr_code():
    data = input("Enter the data for the QR code: ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code generated and saved as 'qrcode.png'.")

def fetch_data_from_api():
    try:
        api_url = input("Enter the API URL: ")
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            print("API Data:")
            print(data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def calculate_math_operation():
    expression = input("Enter a mathematical expression: ")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

def check_weather():
    city = input("Enter the city name: ")
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            print("Weather:")
            print(response.text)
        else:
            print("Weather data not available for this city.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def system_info():
    print("System Information:")
    print(f"Platform: {platform.platform()}")
    print(f"Python Version: {sys.version}")
    print(f"OS Version: {platform.system()} {platform.release()}")

def quit_program():
    print("Exiting the program...")
    exit()

def show_menu():
    clear_screen()
    print("===== Python Menu =====")
    print("1. Show date and time")
    print("2. Create a new text file")
    print("3. Generate a QR code")
    print("4. Fetch data from an API")
    print("5. Calculate a math operation")
    print("6. Check the weather")
    print("7. System information")
    print("8. Quit")
    print("=======================")

def run_menu():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            show_date_time()
        elif choice == "2":
            create_text_file()
        elif choice == "3":
            generate_qr_code()
        elif choice == "4":
            fetch_data_from_api()
        elif choice == "5":
            calculate_math_operation()
        elif choice == "6":
            check_weather()
        elif choice == "7":
            system_info()
        elif choice == "8":
            quit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_menu()
