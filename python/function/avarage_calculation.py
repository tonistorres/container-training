def calculation_avarage():

    sum_of_grades = 0

    for n in range(1, 5):
        value = float(input("Enter the {}ª note:".format(n)))
        sum_of_grades += value

    media = sum_of_grades / 4

    if media < 7:
        print("Failed!!")
    else:
        print("Approved!!")


calculation_avarage()
