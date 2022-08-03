from datetime import datetime

# Constants
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 " \
             "Safari/537.36 "
HEADERS = {"Content-Type": "application/json", "user-agent": USER_AGENT}
STATUS_CODE = 200
PARAM_PINCODE = "pincode="
PARAM_DISTRICT_ID = "district_id="
PARAM_CENTER_ID = "center_id="
PARAM_DATE = "date="
current_date = datetime.now().strftime("%d-%m-%Y")
SYMBOL_AND = "&"
STR_NUMBER_ONE = '1'
STR_NUMBER_TWO = '2'
STR_NUMBER_THREE = '3'
STR_NUMBER_FOUR = '4'
STR_NUMBER_FIVE = '5'
STR_NUMBER_SIX = '6'
STR_NUMBER_SEVEN = '7'
STR_NUMBER_EIGHT = '8'
