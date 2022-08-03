from covid_19_vaccination_slot_availability.service import cowin_vaccination as cow_vac
from covid_19_vaccination_slot_availability.utils import cowin_constant as cow_const
# from datetime import datetime as dtime


def perform_operation(operation_number: str, parameter_list: dict):
    if cow_const.STR_NUMBER_ONE == operation_number:
        print(cow_vac.find_states())

    elif cow_const.STR_NUMBER_TWO == operation_number:
        print(cow_vac.find_districts_by_state_id(parameter_list["state_id"]))

    elif cow_const.STR_NUMBER_THREE == operation_number:
        print(cow_vac.find_districts_by_state_id_list(parameter_list["state_id_list"]))

    elif cow_const.STR_NUMBER_FOUR == operation_number:
        print(cow_vac.find_vaccine_slot_by_pin_code(parameter_list["pin_code"]))

    elif cow_const.STR_NUMBER_FIVE == operation_number:
        print(cow_vac.find_vaccine_slot_by_districts(parameter_list["district_id"]))

    elif cow_const.STR_NUMBER_SIX == operation_number:
        print(cow_vac.find_vaccine_slot_by_calender_and_pin(parameter_list["pin_code"], parameter_list["dt"]))

    elif cow_const.STR_NUMBER_SEVEN == operation_number:
        print(cow_vac.find_vaccine_slot_by_calender_and_district(parameter_list["district_id"], parameter_list["dt"]))

    elif cow_const.STR_NUMBER_EIGHT == operation_number:
        print(cow_vac.find_vaccine_slot_by_calender_and_center_id(parameter_list["center_id"], parameter_list["dt"]))

    else:
        print("Invalid operation ....!!")


def verify_Integer(int_number: str):
    try:
        int(int_number)
        return True
    except ValueError as e:
        print("Error: ", e)
        return False


def validate_date(dte):
    try:
        # dtime.date(dte).strptime(dte, fmt="%d-%m-%Y")
        return True
    except ValueError as e:
        print("Error: ", e)
        return False


if __name__ == "__main__":
    message = """Option table:
                    ----------------------------------------------------------------------
                    ! Operation                                         ! Operation Num. !
                    ----------------------------------------------------------------------
                    ! Get state list                                    ! 1              !
                    ! Get district list using state id                  ! 2              !
                    ! Get district list using list of states            ! 3              !
                    ! Get vaccine slot by PIN CODE for today            ! 4              !
                    ! Get vaccine slot by DISTRICT ID for today         ! 5              !
                    ! Get vaccine slot by PIN CODE and DATE             ! 6              !
                    ! Get vaccine slot by DISTRICT ID and DATE          ! 7              !
                    ! Get vaccine slot by CENTER ID and DATE            ! 8              !
                    ----------------------------------------------------------------------
                    
Please select option: """

    selected_option = input(message)
    print(f"User has selected option: {selected_option}")

    if verify_Integer(selected_option):
        param_list = {"pin_code": None, "district_id": None, "state_id": None, "state_id_list": None, "dt": None, "center_id": None}

        if cow_const.STR_NUMBER_ONE == selected_option:
            perform_operation(selected_option, param_list)

        elif cow_const.STR_NUMBER_TWO == selected_option:
            state_id = input("Please enter a state id: ")
            if verify_Integer(state_id):
                param_list["state_id"] = state_id
                perform_operation(selected_option, param_list)
            else:
                print("Invalid state id....!!")

        elif cow_const.STR_NUMBER_THREE == selected_option:
            state_id_list = input("Please enter list of state id: ")
            param_list["state_id_list"] = state_id_list
            perform_operation(selected_option, param_list)

        elif cow_const.STR_NUMBER_FOUR == selected_option:
            pin_code = input("Please enter a pin code: ")
            if verify_Integer(pin_code):
                param_list["pin_code"] = pin_code
                perform_operation(selected_option, param_list)
            else:
                print("Invalid pin code ....!!")

        elif cow_const.STR_NUMBER_FIVE == selected_option:
            district_id = input("Please enter district id: ")
            if verify_Integer(district_id):
                param_list["district_id"] = district_id
                perform_operation(selected_option, param_list)
            else:
                print("Please provide valid district id ....!!")

        elif cow_const.STR_NUMBER_SIX == selected_option:
            pin_code = input("Please provide pin code: ")
            if verify_Integer(pin_code):
                dt = input("Please provide date in format DD-MM-YYYY: ")
                if validate_date(dt):
                    param_list["pin_code"] = pin_code
                    param_list["dt"] = dt
                    perform_operation(selected_option, param_list)
                else:
                    print("Please provide valid date ....!!")
            else:
                print("Please provide valid pin code ....!!")

        elif cow_const.STR_NUMBER_SEVEN == selected_option:
            district_id = input("Please provide district id: ")
            if verify_Integer(district_id):
                dt = input("Please provide date in format DD-MM-YYYY: ")
                if validate_date(dt):
                    param_list["district_id"] = district_id
                    param_list["dt"] = dt
                    perform_operation(selected_option, param_list)
                else:
                    print("Please provide valid date ....!!")
            else:
                print("Please provide valid district id ....!!")

        elif cow_const.STR_NUMBER_EIGHT == selected_option:
            center_id = input("Please provide center id: ")
            if verify_Integer(center_id):
                dt = input("Please provide date in format DD-MM-YYYY: ")
                if validate_date(dt):
                    param_list["center_id"] = center_id
                    param_list["dt"] = dt
                    perform_operation(selected_option, param_list)
                else:
                    print("Please provide valid date ....!!")
            else:
                print("Please provide valid center id ....!!")

        else:
            print("Invalid operation ....!!")
    else:
        print("Invalid option provided ....!!")
