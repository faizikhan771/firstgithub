# kid_age=5
school_age=5
# question: can kid go to school?
kid_age=input("what is the real age of the kid: ")
kid_age=int(kid_age)
if kid_age==school_age:
    print("congrats! kid can join the scool.")
elif kid_age>=school_age:
    print("he must join the school NOW! ")
else:
    print("sorry! your kid is too young to join the school")

    # if_elif_else statement clear