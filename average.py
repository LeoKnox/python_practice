def average(array):
    thisset = set()
    sum = 0;
    for i in array:
        thisset.add(i);
    for j in thisset:
        sum += j
    return(format(sum/len(thisset),".3f"));
