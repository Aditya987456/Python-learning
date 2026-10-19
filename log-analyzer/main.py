

def read_logs(filename):
    logs_list = []

    with open(filename, "r") as file:
        for line in file:
            logs_list.append(line.strip())

    return logs_list


def count_logs(logs_list):
    total_logs = len(logs_list)

    error_logs = 0
    warning_logs = 0
    info_logs = 0

    for item in logs_list:
        if item.startswith("INFO"):
            info_logs += 1
        elif item.startswith("WARNING"):
            warning_logs += 1
        elif item.startswith("ERROR"):
            error_logs += 1

    return total_logs, error_logs, warning_logs, info_logs


# ----------------function to split the messsage from the logs- before putting in the set-------------------
def split_msg(item):
    message  = item.split(":", 1)[1].strip()
    return message



# -------- all logs messages putting in the set so it will becomes all unique logs---
def find_unique_errors(logs_list):

    unique_logs_set = set()

    for logs in logs_list:
        if(logs.startswith("ERROR")):
            unique_logs_set.add(split_msg(logs))

    return unique_logs_set




# ---------- dictionary for putting the individual error frequency counts ---------
error_freq_count = {}   # empty dictionary initialised for now...



# --------- error frequency count -------- here using dictionary for key value ...
def error_frequency(logs_list):
    error_freq_count = {}

    for item in logs_list:
        if item.startswith("ERROR"):
            message = split_msg(item)

            if message in error_freq_count:
                error_freq_count[message] += 1
            else:
                error_freq_count[message] = 1

    return error_freq_count
        



# --------- count most common errors and its count--------
def max_count_errors(error_dict):

    if not error_dict:
            return None, 0
    
    max_error = max(error_dict, key=error_dict.get)
    max_count = error_dict[max_error]
    
    return max_error, max_count







print("\n")
print("================================================ LOG ANALYZER ===================================================")


# --------- read logs from file ---------
logs_list = read_logs("app.log")



total_logs, error_logs, warning_logs, info_logs = count_logs(logs_list)

print(f"Total logs : {total_logs}")

print(f"Total ERROR logs: {error_logs}")
print(f"Total WARNING logs: {warning_logs}")
print(f"Total INFO logs: {info_logs}")



# ------- unique errors find -------
unique_logs_set = find_unique_errors(logs_list)

print("\n")
print("Unique Errors:")

if not unique_logs_set:
    print("- None")
else:
    for error in unique_logs_set:
        print(f"- {error}")









# ----------- find error frequency -------------
error_freq_count = error_frequency(logs_list)

print("\n")

if error_freq_count:
    print("Error Frequency:")
    print(f"{'ERRORS':<30} | {'COUNT'}")
    print("-" * 40)

    for key, value in error_freq_count.items():
        print(f"{key:<30} | {value}")
# else:
#     print("No errors found.")





# -------------------- most common error-------

# print("\n")
# print("Most Common Error:")

# max_error, max_count = max_count_errors(error_freq_count)

# if max_error is None:
#     print("- No errors found")
# else:
#     print(f"- {max_error} --> [{max_count}]")




print("\n")


max_error, max_count = max_count_errors(error_freq_count)

if max_error is not None:
    print("Most Common Error:")
    print(f"- {max_error} --> [{max_count}]")
    
    









print("\n")










