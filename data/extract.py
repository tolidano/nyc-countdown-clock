import csv
import os
import zipfile


def main():
    lines = []
    try:
        with open('files.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                lines.append({'name': line[0], 'local': line[1], 'remote': line[2]})
    except IOError:
        print('files.csv not found.')
    if lines:
        for line in lines:
            extract(line['name'], line['local'])


def extract(name, path):
    if '.' not in path:
        print('File: ' + name)
        file_path = path + '/temp.zip'
        print ('Extracting {}'.format(file_path))
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_file:
                zip_file.extractall(path)
            print('Finished extracting {}'.format(file_path))
            os.remove(file_path)
            print('Deleted {}'.format(file_path))
        except IOError:
            print('temporary zip file not found.')


if __name__ == '__main__':
    main()
