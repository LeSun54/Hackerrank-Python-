'''
Title     : Find the Runner-Up
Subdomain : Basic Data Types
Domain    : Python
Author    : Leon Sun
Created   : 02 Nov 2018
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num_arr = map(int, arr)
    set_temp = set(num_arr)
    final = list(set_temp)
    final.sort()
    print (final[-2])
