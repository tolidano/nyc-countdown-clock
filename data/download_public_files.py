import argparse
import csv
import os
import requests
import zipfile
from requests.exceptions import ConnectionError


_ONE_MEGABYTE = 1024 * 1024


def main(files):
    lines = []
    try:
        with open('files.csv', 'r') as files:
            contents = csv.reader(files)
            for line in contents:
                lines.append({'name': line[0], 'local': line[1], 'remote': line[2], 'type': line[3]})
    except IOError:
        print('files.csv not found.')
    if lines:
        for line in lines:
            if files == 'all' or files == line['type']:
                download(line['name'], line['local'], line['remote'])


def download(name, local_path, server_path):
    print('File: ' + name)
    try:
        response = requests.get(server_path, stream=True)
    except ConnectionError:
        response = None
        print('Unable to download {}'.format(server_path))
    if response:
        print('Successfully opened streaming connection to {}'.format(server_path))
        if '.' not in local_path:
            try:
                os.makedirs(local_path)
            except FileExistsError:
                pass
            final_path = local_path + '/temp.zip'
        else:
            final_path = local_path
        print('Writing to local path {}'.format(final_path))
        chunks = 0
        with open(final_path, 'wb') as handle:
            for chunk in response.iter_content(chunk_size=_ONE_MEGABYTE):
                if chunk:
                    handle.write(chunk)
                    chunks += 1
        print('Finished downloading {} to {}'.format(server_path, final_path))
        if 'zip' in final_path:
            with zipfile.ZipFile(final_path, 'r') as zip_ref:
                zip_ref.extractall(local_path)
            os.remove(final_path)
            print('Extracted {}'.format(final_path))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('files', help='Either all, status, geography, listings, or schedules', default='status')
    ARGS = PARSER.parse_args()
    main(ARGS.files)
