def f(x,l=[]):

    for i in range(x):

        l.append(i*i)

        print(l)

f(2)

#explanation
# f(2): When this function is called without providing the second argument l, the default list [] is used. 
# The loop runs for i in the range from 0 to 1. It appends 0*0 = 0 and 1*1 = 1 to the list l. The output will be [0, 1].

f(3,[3,2,1])

#explanation
# f(3, [3, 2, 1]): In this call, the provided list [3, 2, 1] is used as the second argument l. 
# The loop runs for i in the range from 0 to 2. It appends 0*0 = 0, 1*1 = 1, and 2*2 = 4 to the list l that was passed as an argument. 
# The output will be [3, 2, 1, 0, 1, 4].

f(3)

#explanation
# f(3): In this call, the second argument l is not provided, so the default list [] is used. 
# However, the interesting part is that the default list l is created only once when the 
# function is defined, and subsequent calls to the function will keep using the same list. 
# Therefore, the loop runs for i in the range from 0 to 2. It appends 0*0 = 0, 1*1 = 1, and 2*2 = 4 to 
# the same default list l used in the previous call. The output will be [0, 1, 4].
