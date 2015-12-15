#!/usr/bin/env python
def age(listyears):
    "Takes list of years between 1950 and 2015, returns median age and two ages closest, where age =2015-year. List randomly ordered, odd number of elements N, N>3"
#    print type(listyears)
    N=len(listyears)
#    print type(N)
    if N<3:
        return("You done goofed, Please try again and enter a list of N years with N>3")
    elif N%2==0:
        return("You done goofed, Please try again and enter a list of N years with N odd")
    else:
        listages=[]
        for i in range(N):
            listages.append(2015-listyears[i])
        listages.sort()
        M=N-1
        return(listages[M/2-1],listages[M/2],listages[1+M/2])
        
print age([1989,1955,2011,1943,1975])
