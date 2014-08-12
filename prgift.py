"""http://www.codechef.com/AUG14/problems/PRGIFT/
"""
t = int(raw_input())
count_list=[]
for j in xrange(t):
    n,k=map(int,raw_input().split())
    a=map(int,raw_input().split())
    m=0
    for i in xrange(n):
        if (a[i]%2==0):
            m=m+1
    if k==0 and m==n:
        count_list.append("NO")
    elif m>=k:
        count_list.append("YES")
    else:
        count_list.append("NO")        
 
    
for i in xrange(t):
    print count_list[i] 