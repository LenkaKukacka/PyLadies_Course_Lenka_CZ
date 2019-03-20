runFast = int(input("How many kms you run today?"))

if runFast > 5 and runFast < 10:
    print ("You rock!")
elif runFast > 10 and runFast < 40:
    print ("Bravo!")
elif runFast > 40:
    print ("Wooooooooow, You are ready for a Marathon!!!")
elif runFast < 5:
    print ("Goood, keep on running.")
else:
    print ("How many?")
