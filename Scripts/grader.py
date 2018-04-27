def qpa():
    values = {"A":4, "B":3, "C":2, "D":1, "R":0, "X":0, "P":0, "N":0, "O":0,
              "W":0, "I":0, "AD":0}
    nonfactorable = {"P", "N", "O", "W", "I", "AD"}
    grades = []
    units = []
    sumGrades = 0
    sumUnits = 0

    n = input("How many Classes? ")
    while not n.isnumeric() or int(n) < 0:
        print("Please enter a valid number of classes")
        n = input("How many Classes? ")
    n = int(n)

    for i in range(n):
        print("#################")
        print('#\tClass %2d\t#' % (i + 1))
        print("#################")

        cur = input("What is your Grade? ").upper()
        while cur not in values and cur not in nonfactorable:
            print("Please Enter a Valid Grade")
            cur = input("What is your Grade? ").upper()
        grades.append(values[cur])

        u = input("How many Units? ")
        while not u.isnumeric() or int(u) < 0:
            print("Please Enter a Valid Amount of Units")
            u = input("How many Units? ")

        if cur in nonfactorable:
            u = 0
        units.append(int(u))

        sumGrades += grades[i] * units[i]   # Multiply by 0 so won't affect
        sumUnits += units[i]

    if sumUnits != 0:
        print("QPA: %1.3f" % (sumGrades / sumUnits))
    else:
        print("QPA: 0.00")


def main():
    while True:
        qpa()
        if input("Quit: (Y/n)? ").upper() != "N":
            break
        print("#################")

if __name__ == "__main__":
    main()