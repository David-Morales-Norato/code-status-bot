import json
import time
import os



epochs = 13
relative_error = 10e-2
psnr = 25.31
loss_function = 1.18
vars = {}

vars["epochs"] = epochs
vars[ "relative_error"] = relative_error
vars["psnr"] = psnr
vars["loss_function"]= loss_function

errors = ["File 1.npy doesn't exists", "File 2.npy doesn't exists"]
data = {}

data = { "vars":vars, "errors": errors}
data["var_activity_bot"] = "epochs"

file_path = os.path.join(os.getcwd(),"status_code.json")



while(1):
    
    with open(file_path,'w') as f:
        json.dump(data, f, indent=4)
    time.sleep(3)
    data["vars"]["epochs"] += 1 
    data["vars"]["relative_error"] -= 0.01 
    data["vars"]["loss_function"] += 0.01 
    

