# take first input for how many starting donuts
d = int(input())

# after test 1 ----------
if d < 0:
    d *= -1
#-----------------------

# take second input for event occurences
e = int(input())

# after test 2-----------
if e == 0:
    print(d)
#-----------------------

else:

# after test 3 ----------
    if e < 0: 
        e *= -1
#-----------------------

    # assign r to initial value
    r = d

    # iterate e times
    for i in range(e):
        # take input for sign and value
        sign = input()
        q = int(input())

        # after test 4-------
        if q < 0:
            q *= -1
        #-------------------

        # increment r by q
        r += q

        # if the sign was negative then subtract twice
        if sign == "-":
            r -= 2*q

    # print the final value after iteration
    print(r)