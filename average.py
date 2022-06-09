def average(array):
    thisset = set(array)
    sum = 0;
    for j in thisset:
        sum += j
    return(format(sum/len(thisset),".3f"));
