for i in range (10, 25):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, "bukan prima")
    elif i % 2 > 0 or i % 3 > 0 or i % 5 > 0 or i % 7 > 0:
        print(i, "adalah bilangan prima")
    else:
        pass
