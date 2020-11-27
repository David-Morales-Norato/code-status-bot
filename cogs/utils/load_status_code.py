import json
import os

# This function returns the dictionary of a certain JSON file
def read_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            return json.load(f)
    else:
        raise(f"JSON file not found. path: {file_path}")


# Read the status file and set default values if vars doesn't appear
def read_status_file(status_file_path, var_activity_bot):
    status_code = None

    status_code = read_json_file(status_file_path)
    status_code[var_activity_bot] = status_code.get(var_activity_bot,"")
    status_code["vars"] = status_code.get("vars",{})
    status_code["errors"] = status_code.get("errors",[])


    return status_code


# Read the setup file and set default values if optional vars doesn't appear
def read_setup_file(setup_file_path):

    setup_dict = read_json_file(setup_file_path)

    # Obligatory vars
    setup_dict["json_file_path"] = setup_dict.get("json_file_path",None)
    setup_dict["default_channel_id"] = int(setup_dict.get("default_channel_id",None))

    # Optional vars
    setup_dict["check_status_file"] = setup_dict.get("check_status_file",True)
    setup_dict["var_activity_bot"] = setup_dict.get("var_activity_bot","var_activity_bot")
    setup_dict["vars_string"] = setup_dict.get("vars_string","vars_status")
    setup_dict["errors_string"] = setup_dict.get("errors_string","error_history")
    setup_dict["minutes_to_wait_in_loop"] = setup_dict.get("minutes_to_wait_in_loop",10)
    setup_dict["error_url_img"] = setup_dict.get("error_url_img","https://cdn3.iconfinder.com/data/icons/basicolor-signs-warnings/24/182_warning_notice_error-512.png")

    return setup_dict
