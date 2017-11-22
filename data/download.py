import csv
import requests


def main():
    with open('files.csv', 'r') as files:
        contents = csv.reader(files)
        for line in contents:
            print(line[0] + '.....' + line[1] + '....' + line[2])


if __name__ == '__main__':
    main()
