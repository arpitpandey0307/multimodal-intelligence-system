#reading the file
with open("application.log","r") as file:
    logs=file.readlines()

# print("These all are logs in form of list:")
# for log in logs:
#     print(log.split())

#now we are going to parse
# logger="2026-08-18 10:01:01 INFO UserService Request successful"
# parse=logger.split()
# print(parse)
# print('Date: ',parse[0])
# print('Time: ',parse[1])
# print('Log level: ',parse[2])
# print('Service: ',parse[3])
# print('Message: ',)

count=0
for log in logs:
    logger=log
    parse=logger.split(" ")
    if parse[2]=="ERROR":
        count+=1
# print(count)


#using the counter function to calculate the number of erros in a particular time frame
from collections import Counter

error_by_minute=Counter() #making object
for log in logs:
    parts=log.split()
    if "ERROR" in log:
        minute=parts[1][:5] #time and take only hours and minute
        error_by_minute[minute]+=1

    # if "INFO" in log:
    #     minute=parts[1][:5]
    #     error_by_minute[minute]+=1


print(error_by_minute)

#now using dictionary
error_dict={}
for log in logs:
    parts=log.split()
    if "INFO" in log:
        minute=parts[1][:5]
        error_dict[minute]=error_dict.get(minute, 0) + 1
print(error_dict)

error_by_minute.update(error_dict)

print(error_by_minute)

#performaing the single rule based detection (anomaly)
threshold=3 #defining a threshold

for minute, count in error_by_minute.items():
    if count>threshold:
        print("ANOMALY: ", minute, "had", count, "errors")

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[x**2 for x in list1]
print(list2)

#using isolation forest for anomaly detection
from sklearn.ensemble import IsolationForest
errors=[[2],[5],[100],[4],[10],[200]] #making some errors
model=IsolationForest(contamination=0.1, random_state=42)
model.fit(errors) #model starts analyzing the errors variable

predict=model.predict(errors)
print(predict)

import matplotlib.pyplot as plt
plt.plot(errors)
plt.xlabel('errors')
plt.ylabel('Values')
plt.title('error plotting')
plt.show()