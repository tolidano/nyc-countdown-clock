import csv
import json


def main():
    lines = []
    header = False
    try:
        with open('StationComplexes.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                if header:
                    lines.append({'complex_id': line[0], 'complex_name': line[1]})
                header = True
    except IOError:
        print('StationComplexes.csv not found.')
    print(json.dumps(lines, indent=1))


if __name__ == '__main__':
    main()
