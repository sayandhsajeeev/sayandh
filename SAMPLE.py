name=input("what is your name:")
time=float(input("what is the current time !(0-23)"))
if  5<= time <12:
    grating="good morning"
elif 12<= time <15.30:
    grating="good afternoon"
elif 15.30<= time <18:
    grating="good evening"
else:
    grating=("good night")

print(grating+","+name)