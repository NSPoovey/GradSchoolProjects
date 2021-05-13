class Flower:
    def __init__ (self, name = 'blank', petals = 0, price = 0):
        self._name = name
        self._petals = petals
        self._prcie = price
if __name__ == '__main__':
    choice = 'y'
    while choice != 'n':
        f1 = Flower()
        print('Enter the name of the flower.')
        f1._name = input()
        print('Enter the number of petals on the flower.')
        f1._petals = input()
        print('Enter the price of the flower.')
        f1._price = input()
        print()
        print('The', f1._name, 'flower has', f1._petals, 'petals and costs $', f1._price )
        print()
        choice = input("Would you like to enter another flower? (y/n)")