import csv
import json


def main():
    """
    MTA Mode,Line/Branch,RGB Hex,Pantone CVC,CMYK
    """
    colors = []
    try:
        with open('colors.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                if line[4]:
                    colors.append({
                        'mode': line[0],
                        'line': line[1],
                        'branch': line[1],
                        'rgb': line[2],
                        })
    except IOError:
        print('colors.csv not found.')
    print(json.dumps(colors, indent=1))


if __name__ == '__main__':
    main()
