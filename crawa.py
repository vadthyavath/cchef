"""
http://www.codechef.com/AUG14/problems/CRAWA
"""


t = int(raw_input())
count_list=[]
for j in xrange(t):
    x,y=map(int,raw_input().split())
    if x==0 and y==0:
        count_list.append("YES")
 
    elif x<0 and x%2==0 and (x<=y<=-x) :
        count_list.append("YES")
    elif x>0 and x%2!=0 and ((-x+1)<=y<=(x+1)):
        count_list.append("YES")
 
    elif y>0 and y%2==0 and (-y<=x<=y-1):
        count_list.append("YES")
    elif y<0 and y%2==0 and (y<=x<=-y+1):
        count_list.append("YES")
    else:
        count_list.append("NO")
 
    
for i in xrange(t):
    print count_list[i]  