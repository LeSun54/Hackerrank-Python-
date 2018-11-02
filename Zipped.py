'''
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Leon Sun
Created   : 02 Nov 2018
'''

n, x = map(int,input().split())
ag = [0 for i in range(n)]
for i in range(x):
    temp_ag=list(map(float,input().split()))
    for j in range(n):
        ag[j] += temp_ag[j]
for i in range(n):
    print(ag[i]/x)
