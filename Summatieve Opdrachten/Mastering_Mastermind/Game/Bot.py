from Database import data as all_answers
print(all_answers)
class main:

    def Player():
        Symbols = ["+", "-", "x", "o", "*", "?"]
        In1 = input("Enter the first symbol: ")
        while In1 not in Symbols:
            In1 = input("Enter the first symbol: ")
        In2 = input("Enter the second symbol: ")
        while In2 not in Symbols:
            In2 = input("Enter the second symbol: ")
        In3 = input("Enter the third symbol: ")
        while In3 not in Symbols:
            In3 = input("Enter the third symbol: ")
        In4 = input("Enter the fourth symbol: ")
        while In4 not in Symbols:
            In4 = input("Enter the fourth symbol: ")
        return [In1] + [In2] + [In3] + [In4]


if __name__ == '__main__':
    main