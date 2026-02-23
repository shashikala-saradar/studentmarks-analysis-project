logs=[
    "INFO User logged in",
    "ERROR Failed to load page",
    "WARNING Low disk space",
    "INFO File uploaded",
    "ERROR Database connection failed",
    "INFO User logged out"
]

error_count=0
warning_count=0
info_count=0
for log in logs:
    if "ERROR" in log:
        error_count+=1
    elif "WARNING" in log:
        warning_count+=1
    elif "INFO" in log:
        info_count+=1
print("Total log entries",len(logs))
print("info logs",info_count)
print("warning logs",warning_count)
print("Error logs",error_count)

keyword=input("Enter keyword to search")


print("\nmatching log entries:")
for log in logs:
    if keyword.lower() in log.lower():
        print(log)


