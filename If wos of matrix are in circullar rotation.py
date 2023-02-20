arr = [[1,2,3],[3,1,2],[2,3,1]]
st=""
for i in range(0,1):
    for j in range(0,3):
        st=st+str(arr[i][j])    
st = st + st
st1=""
st2=""
for i in range(1,3):
    for j in range(1,3):
        if i == 1:
            st1=st1+str(arr[i][j])
        else:
            st2=st2+str(arr[i][j])
            
if (st1 in st and st2 in st):
    print("It is a cycle")
