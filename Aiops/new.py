'''
Problem Statement

You are working as an AIOps Engineer for an online university portal. The monitoring system has recorded the following server response times in milliseconds over 20 time intervals:

response_time = [
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]

Most of the requests have a response time between approximately 118–131 ms, but some values appear significantly different.

Your task is to build a Python-based anomaly detection system using Isolation Forest.
'''


from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
response_time = [
    120, 125, 118, 130, 122,
    127, 124, 121, 129, 126,
    123, 128, 125, 122, 131,
    700, 127, 119, 650, 124
]
values=([[x] for x in response_time])

model = IsolationForest(contamination=0.1,random_state=42)

model.fit(values)

anomalies = model.predict(values)

print("Anomalies:")

for i in range(len(response_time)):
    if anomalies[i] == -1:
        print(f"Response time {response_time[i]} ms is an anomaly.")

#plt.plot(response_time)
plt.plot((anomalies))
plt.show()