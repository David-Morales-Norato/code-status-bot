import json
import os

def read_status_file(status_file_path, var_activity_bot):
    status_code = None

    if os.path.exists(status_file_path):
        with open(status_file_path,'r') as f:
            status_code = json.load(f)
    else:
        raise(f"Status file not found. path: {status_file_path}")



    status_code[var_activity_bot] = status_code.get(var_activity_bot,"")
    status_code["vars"] = status_code.get("vars",{})
    status_code["errors"] = status_code.get("errors",[])


    return status_code