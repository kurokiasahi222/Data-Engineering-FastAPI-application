import time
from typing import List, Dict, DefaultDict
from tqdm import tqdm
import os
import sys
from datetime import datetime
from pprint import pprint

CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_FOLDER_NAME)
# Add parent directory to sys.path if not already included
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)
    sys.path.append(PARENT_DIR + "/w1")

from w1.data_processor import DataProcessor
import constants
from global_utils import get_file_name, make_dir, plot_sales_data


class DP(DataProcessor):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def get_file_path(self) -> str:
        return self._fp

    def get_file_name(self) -> str:
        return self._file_name

    def get_n_rows(self) -> int:
        return self._n_rows


def revenue_per_region(dp: DP) -> Dict:
    data_reader = dp.data_reader
    data_reader_gen = (row for row in data_reader)

    # skip first row as it is the column name
    _ = next(data_reader_gen)

    aggregate = dict()

    for row in tqdm(data_reader_gen):
        if row[constants.OutDataColNames.COUNTRY] not in aggregate:
            aggregate[row[constants.OutDataColNames.COUNTRY]] = 0
        aggregate[row[constants.OutDataColNames.COUNTRY]] += dp.to_float(row[constants.OutDataColNames.TOTAL_PRICE])

    return aggregate


def get_sales_information(file_path: str) -> Dict:
    # Initialize
    dp = DP(file_path=file_path)

    # print stats
    dp.describe(column_names=[constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.TOTAL_PRICE])

    # return total revenue and revenue per region
    return {
        'total_revenue': dp.aggregate(column_name=constants.OutDataColNames.TOTAL_PRICE),
        'revenue_per_region': revenue_per_region(dp),
        'file_name': get_file_name(file_path)
    }


# batches the files based on the number of processes
def batch_files(file_paths: List[str], n_processes: int) -> List[set]:
    # if the n_process is larger than len(file_paths) just use the length of file_paths
    if n_processes > len(file_paths):
        n_processes = len(file_paths)
        
    n_per_batch = len(file_paths) // n_processes

    first_set_len = n_processes * n_per_batch
    first_set = file_paths[0:first_set_len]
    second_set = file_paths[first_set_len:]

    batches = [set(file_paths[i:i + n_per_batch]) for i in range(0, len(first_set), n_per_batch)]

    # batches = []
    # for i in range(0, len(first_set), n_per_batch):  # n_per_batch is a step
    #     batch = set(file_paths[i: i + n_per_batch])
    #     batches.append(batch)
    for i, file in enumerate(second_set):
        batches[i].add(file)
    
    return batches, n_processes


# Fetch the revenue data from a file
def run(file_names: List[str], n_process: int) -> List[Dict]:
    st = time.time()

    print("Process : {}".format(n_process))
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    file_paths = [os.path.join(folder_path, file_name) for file_name in file_names]
    revenue_data = [get_sales_information(file_path) for file_path in file_paths]

    en = time.time()

    print(f"Batch for process-{n_process} time taken {en - st}")
    return revenue_data


def flatten(lst: List[List]) -> List:
    return [item for sublist in lst for item in sublist]
