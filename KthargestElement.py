def kthlargest(ar,k=1):
    if(k>len(ar)):
        return("Pass Right Array And Index")
    if(k==1):
        l=[]
        for i in ar:
            l.append(i)
        m1=l[0]
        for i in l:
            if(m1<i):
                m1=i
        return(m1)
    else:
        l=[]
        mv=ar[0]
        for i in ar:
            if(mv>i):
                mv=i
        for i in range(k+1):
            l.append(mv)
        l[0]=kthlargest(ar,1)
        for i in range(k):
            for j in ar:
                if(j<l[i] and j>l[i+1]):
                    l[i+1]=j
        #return(l)
        return(l[k-1])


x=[1,2,8,4,3,1,1,2,3,4,7,8,3,2,12,112,5,53,221,1,43,543,21,545,665,556,6767]
i=7
print("Array Element ",x)
print("Largest Element At ",i,"th Position is ",sep="",end=" ")
print(kthlargest(x,i))
