for number in range(1, 6):
    print("\nTable of", number)

    for multiplier in range(1, 11):

        if multiplier == 5:
            continue

        print(number, "x", multiplier, "=", number * multiplier)