
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file', nargs='?', const="books.csv", type=str)
parser.add_argument('--n', dest='n', type=int)
parser.add_argument('--index', dest='index', type=str)
args = parser.parse_args()

print("POST _bulk")

with open(args.file, 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if args.n is not None and i > args.n:
            break
        if i == 0:
            headers = row
            id_index = headers.index('id')
            data_indices = {headers[i]: i for i in range(len(headers)) if i != id_index}
        else:
            print(f'{{ "index" : {{ "_index" : "{args.index}", "_id" : "{row[id_index]}"}}}}')
            print("{", ", ".join([f'"{h}": "{row[i]}"' for h, i in data_indices.items()]), "}")