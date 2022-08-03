from datetime import datetime
import requests
from covid_19_vaccination_slot_availability.utils import cowin_api
from covid_19_vaccination_slot_availability.utils import cowin_constant


def process_request(url: str):
    response = requests.get(url=url, headers=cowin_constant.HEADERS)
    return response.json() if response.status_code == cowin_constant.STATUS_CODE else response.raise_for_status()


def find_states():
    print("Finding states...")
    return process_request(cowin_api.COWIN_VACCINE_STATES)


def find_districts_by_state_id_list(state_id_list: list):
    print("Finding districts by list of state IDs...")
    print("List = ", state_id_list)

    district_list = {}

    for state_id in state_id_list:
        print(f"Getting district by state {state_id}")
        district_list[state_id] = find_districts_by_state_id(state_id)

    return district_list


def find_districts_by_state_id(state_id: str):
    print("Finding districts by state ID...")
    print("State id = ", state_id)

    new_url = cowin_api.COWIN_VACCINE_DISTRICT.replace("{state_id}", state_id)
    return process_request(new_url)


def find_vaccine_slot_by_pin_code(pin_code: str):
    print("Finding vaccine slot by pin_code...")
    print("Pin code: ", pin_code)

    new_url = cowin_api.COWIN_VACCINE_SLOT_BY_PIN.__add__(cowin_constant.PARAM_PINCODE).__add__(pin_code).__add__(cowin_constant.SYMBOL_AND).__add__(cowin_constant.PARAM_DATE).__add__(cowin_constant.current_date)
    return process_request(new_url)


def find_vaccine_slot_by_districts(district_id: str):
    print("Finding vaccine slot by district ID...")
    print(f"District Id: {district_id}")

    new_url = cowin_api.COWIN_VACCINE_SLOT_BY_DISTRICT + cowin_constant.PARAM_DISTRICT_ID + district_id + cowin_constant.SYMBOL_AND + cowin_constant.PARAM_DATE + cowin_constant.current_date
    return process_request(new_url)


def find_vaccine_slot_by_calender_and_pin(pin_code: str, dt: datetime):
    print("Finding vaccine slot by date and pin_code...")
    print(f"Pin code: {pin_code},\tDate: {dt}")

    new_url = cowin_api.COWIN_VACCINE_SLOT_BY_CALENDER_PIN + cowin_constant.PARAM_PINCODE + pin_code + cowin_constant.SYMBOL_AND + cowin_constant.PARAM_DATE + dt
    return process_request(new_url)


def find_vaccine_slot_by_calender_and_district(district_id: str, dt: datetime):
    print("Finding vaccine slot by date and district_id...")
    print(f"District Id: {district_id},\tDate: {dt}")

    new_url = cowin_api.COWIN_VACCINE_SLOT_BY_CALENDER_DISTRICT + cowin_constant.PARAM_DISTRICT_ID + district_id + cowin_constant.SYMBOL_AND + cowin_constant.PARAM_DATE + dt
    return process_request(new_url)


def find_vaccine_slot_by_calender_and_center_id(center_id: str, dt: datetime):
    print("Finding vaccine slot by date and center_id...")
    print(f"Center Id: {center_id},\tDate: {dt}")

    new_url = cowin_api.COWIN_VACCINE_SLOT_BY_CALENDER_CENTER_ID + cowin_constant.PARAM_CENTER_ID + center_id + cowin_constant.SYMBOL_AND + cowin_constant.PARAM_DATE + dt
    return process_request(new_url)


if __name__ == "__main__":
    # print(find_states())
    # print(find_districts_by_state_id_list(['21', '6', '27', '30']))
    # print(find_districts_by_state_id('21'))
    # print(find_vaccine_slot_by_pin_code('411027'))
    # print(find_vaccine_slot_by_districts('21'))
    # print(find_vaccine_slot_by_calender_and_pin('411027', cowin_constant.current_date))
    # print(find_vaccine_slot_by_calender_and_district('21', cowin_constant.current_date))
    # print(find_vaccine_slot_by_calender_and_center_id('123', cowin_constant.current_date))

    print("API has finished execution...!!")
