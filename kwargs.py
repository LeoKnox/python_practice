def work_args(**kwargs):
    for key in kwargs:
        print ("a = {0}, b={1}".format(key, kwargs[key]))

work_args(a="1", b="2")
