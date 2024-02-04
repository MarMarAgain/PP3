import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
   "https://www.googleapis.com/auth/spreadsheets",
   "https://www.googleapis.com/auth/drive.file",
   "https://www.googleapis.com/auth/drive"
   ]


CREDS = Credentials.from_service_account_file('creds1.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from user
    """
    print('please enter sales data from last market')
    print('Data shuld be six numbers, seperated by commas')
    print('10,20,30,40,50\n')

    data_str = input('Enter your data here:')
    
    sales_data= data_str.split(",")
    validate_data(sales_data)


def validate_data(values):
     """
    Inside the try, convert all string values to intergers.
    Raise ValueError if strings cannot be converted to interger or if there aren't exactly 6 values
    """
     try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
     except ValueError as e:
        print(f"Invalid data {e}, please try again.\n")

get_sales_data()