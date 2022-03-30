import csv


def readfile(join):
    with open('file1.csv', newline='') as csvfile1, open('file2.csv', newline='') as csvfile2:
        file1 = csvfile1.readlines()
        file2 = csvfile2.readlines()

        # file1 = csv.DictReader(csvfile1, delimiter=',', quotechar='|')
        # file2 = csv.DictReader(csvfile2, delimiter=',', quotechar='|')

        for line in file1:
            print(line)
                    # match join:
                    #     case 'inner':
                    #         print(row1, row2)
                    #     case 'left':
                    #         print("a == b i a")
                    #     case 'right':
                    #         print("a == b i b")


readfile("inner")
