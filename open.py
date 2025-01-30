import subprocess

# List of parameters to vary
parameters = ["01","02","03","04","06","07","08", "09", "10", "12","13"]

# Base command template (adjust as needed)
base_command = "unzip sheet{parameter}.zip -d {folder}"

# Loop through the parameters and run each command
for param in parameters:
    match param:
        case "01":
            command = base_command.format(parameter=param,folder = "bayes-decision")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "02":
            command = base_command.format(parameter=param,folder = "parameter-estimation")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "03":
            command = base_command.format(parameter=param,folder = "fisher-discriminant")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "04":
            command = base_command.format(parameter=param,folder = "pca")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "06":
            command = base_command.format(parameter=param,folder = "svm")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "07":
            command = base_command.format(parameter=param,folder = "model-selection")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "08":
            command = base_command.format(parameter=param,folder = "neural-networks-1")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "09":
            command = base_command.format(parameter=param,folder = "neural-networks-2")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "10":
            command = base_command.format(parameter=param,folder = "desision-tree")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "12":
            command = base_command.format(parameter=param,folder = "clustering")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        case "13":
            command = base_command.format(parameter=param,folder = "kernel-ridge-regression")
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

