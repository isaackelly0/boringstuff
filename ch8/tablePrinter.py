def printTable(data):
    colWidths = [0] * len(data)
    #nested for loops to find longest word in each sequence
    for i in range(len(data)):
        for j in data[i]:
            if len(j) > colWidths[i]:
                colWidths[i] = len(j)
        #join, justify, and print new line
        print('\n'.join(d.rjust(colWidths[i]) for d in data[i]))
    return None
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)