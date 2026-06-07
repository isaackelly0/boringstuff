def stringify(theList):
    sentence = ''
    for i in theList:
        if i == theList[-1]:
            sentence += 'and ' + i
        else:
            sentence += i + ', '
    return sentence