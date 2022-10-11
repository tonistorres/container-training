nossaString = "Eu gosto de sorvete"


def cycle_through_characters(str):
    for i in list(nossaString):
        print(i)


# cycle_through_characters(nossaString)


def exemple():
    fruit = "apple"
    for idx in range(len(fruit)):
        print(fruit[idx])


# exemple()


def exemple_2():
    fruit = "Tonis Torres"
    for idx in range(len(fruit) - 1, -1, -1):
        print(fruit[idx])


exemple_2()
