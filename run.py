import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hotel_reservations')


reservations = GSPREAD_CLIENT.open('hotel_reservations').worksheet('reservations')


def full_name():
    """
    Takes the full name and details of the client and updates spreadsheet
    """
    while True: 

        print("Please enter your full name\n")
        print("For example: Tarik Khan \n")

        customer_name = input("Enter your full name here: \n")
        print(f"You have entered '{customer_name}'\n")

    return customer_name


def validate_full_name(customer_name):
    """
    Validates the input entered as the customers full name
    """

    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)

    res = regex_name.search(customer_name)

    if res:
        print("Valid input. Updating datasheet...\n")
    else: 
        print("Invalid. Please enter a valid name.\n")


full_name()
validate_full_name()




