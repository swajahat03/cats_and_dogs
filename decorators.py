import csv , traceback
from datetime import datetime
from flask import request 

def logHeaders(func):
    print("at decorator")
    def wrapper(*args, **kwargs):
        try:
            print(sorted(request.headers.keys()))
            with open("logs2.csv", "a") as csvfile:
                csvWriter = csv.writer(csvfile)
                headerData = []
                headerData.append(datetime.now())
                for key in sorted(request.headers.keys()):
                    headerData.append(request.headers[key])
                csvWriter.writerow(headerData)
            func(*args, **kwargs)
        except:
            traceback.print_exc()
    return wrapper