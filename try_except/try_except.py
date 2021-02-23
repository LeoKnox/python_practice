try:
    print(x)
except NameError:
    print("CREATE X")
except something_else:
    print("something_else went wrong")
else:
    print("We did something")
