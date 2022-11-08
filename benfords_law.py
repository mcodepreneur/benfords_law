'''
Author: Michael Denenberg
Description: This program receives a csv with number values, scrapes
             those values into a list, and enumerates values with the
             same starting number. The program then calculates the
             percentages these numbers take up in comparison to the
             dataset and displays them to the user, along with an
             analysis of whether the dataset follows Benford's law or
             not.
'''
def main():
    data = open(input('Data file name:\n'), 'r').readlines()
    numbers = []
    for line in data:
        line = line.strip('\n').split(',')
        for item in line:
            if item[0].isnumeric() and item[0] != '0' and item[len(item) - 1].isnumeric():
                numbers.append(float(item))

    dist = []
    for i in range(1, 10):
        dist.append(0)
        for x in numbers:
            if str(x)[0] == str(i):
                dist[i-1] += 1

    percent = [x / len(numbers) * 100 for x in dist]
    guide = [30, 17, 12, 9, 7, 6, 5, 5, 4]
    ben = True
    print()
    for i in range(9):
        if not (guide[i] + 10 >= int(percent[i]) >= guide[i] - 5):
            ben = False
        print(str(i + 1) + ' | ' + '#' * int(percent[i]))

    print('\n' + "Follows Benford's Law" * ben +
          "Does not follow Benford's Law" * (not ben))

main()
