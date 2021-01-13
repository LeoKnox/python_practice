def work_args(**kwargs):
    for key in kwargs:
        print ("{0} = {1}".format(key, kwargs[key]))

work_args(one = "1", two = "2", three = "3")
