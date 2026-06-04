def collatz(number):
    if number % 2 == 0:
        div = number / 2
        print(div)
        return div
    else:
        x = 3 * number + 1
        print(x)
        return x