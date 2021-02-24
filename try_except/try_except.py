if x < 0:
    raise exception("No negs!")

try:
    print(x)
except:
    print("something_else went wrong")
else:
    print("Well your kind of screwed")
finally:
    print("Something above was done")
