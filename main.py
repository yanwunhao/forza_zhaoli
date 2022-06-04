from surprise import SVDpp, NMF
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

import os

print("SVD++ on Hokkaido Dataset")

file_path = os.path.expanduser('new_dataset')

reader = Reader(line_format='user item rating', sep=' ')

data = Dataset.load_from_file(file_path, reader=reader)

cross_validate(SVDpp(), data, verbose=True)

print("NMF on Hokkaido Dataset")

file_path = os.path.expanduser('new_dataset')

reader = Reader(line_format='user item rating', sep=' ')

data = Dataset.load_from_file(file_path, reader=reader)

cross_validate(NMF(), data, verbose=True)