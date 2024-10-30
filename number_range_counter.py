#Define/initialize counters for each range
#Loop to get the user input
#Check if the input is a valid integer
#Check the range of the input number
#Display the numbers

numbers_1_10 = 0
numbers_11_20 = 0
numbers_21_30 = 0
numbers_31_40 = 0
numbers_41_50 = 0

while True:
    try:
        number = int(input("Please enter a number between 1 and 50: "))

        if 1 <= number <= 10:
            numbers_1_10 += 1
        elif 11 <= number <= 20:
            numbers_11_20 += 1
        elif 21 <= number <= 30:
            numbers_21_30 += 1
        elif 31 <= number <= 40:
            numbers_31_40 += 1
        elif 41 <= number <= 50:
            numbers_41_50 += 1
        else:
            print("Invalid input. Heading to Input Summary")
            break
    except ValueError:
        print("Invalid input. Heading to Input Summary")
        break


   