from surprise import BaselineOnly
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

import os

file_path = os.path.expanduser('ml-100k/new_udataset')

reader = Reader(line_format='user item rating', sep=' ')

data = Dataset.load_from_file(file_path, reader=reader)

cross_validate(BaselineOnly(), data, verbose=True)