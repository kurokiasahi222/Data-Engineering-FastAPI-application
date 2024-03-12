from data_processor import DataProcessor
from pprint import pprint, pformat
from typing import Dict
from tqdm import tqdm
import os
import sys
import argparse
from datetime import datetime
import json
import time
from utils import *

# "../../something"

CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_FOLDER)
# Add parent directory to sys.path if not already included
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)

import constants
from global_utils import get_file_name, make_dir, plot_sales_data


def revenue_per_region(dp: DataProcessor) -> Dict:
    """
    Input : object of instance type Class DataProcessor
    Output : Dict

    The method should find the aggregate revenue per region

    For example if the file format is as below:

    StockCode    , Description    , UnitPrice  , Quantity, TotalPrice , Country
    22180        , RETROSPOT LAMP , 19.96      , 4       , 79.84      , Russia
    23017        , APOTHECARY JAR , 24.96      , 1       , 24.96      , Germany
    84732D       , IVORY CLOCK    , 0.39       , 2       , 0.78       ,India
    ...
    ...
    ...

    expected output format is:
    {
        'China': 1.66,
        'France': 17.14,
        'Germany': 53.699999999999996,
        'India': 55.78,
        'Italy': 90.45,
        'Japan': 76.10000000000001,
        'Russia': 87.31,
        'United Kingdom': 29.05,
        'United States': 121.499
    }
    """
    ######################################## YOUR CODE HERE ##################################################
    data_reader_gen: Generator = (row for row in dp.data_reader)

    # skip first row as it is the column name
    _ = next(data_reader_gen)

    # initialize the aggregate variable
    aggregate: Dict = {}
    country: str = constants.OutDataColNames.COUNTRY
    total_price: str = constants.OutDataColNames.TOTAL_PRICE

    for row in tqdm(data_reader_gen):
        if row[country] not in aggregate:
            aggregate[row[country]] = float(row[total_price])
        aggregate[row[country]] += float(row[total_price])

    return aggregate
    ######################################## YOUR CODE HERE ##################################################


def get_sales_information(file_path: str) -> Dict:
    # Initialize
    dp = DataProcessor(file_path=file_path)

    # print stats
    dp.describe(column_names=[constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.TOTAL_PRICE])

    # return total revenue and revenue per region
    return {
        'total_revenue': dp.aggregate(column_name=constants.OutDataColNames.TOTAL_PRICE),
        'revenue_per_region': revenue_per_region(dp),
        'file_name': get_file_name(file_path)
    }


def main():
    parser = argparse.ArgumentParser(description="Choose from one of these : [tst|sml|bg]")
    parser.add_argument('--type',
                        default='tst',
                        choices=['tst', 'sml', 'bg'],
                        help='Type of data to generate')
    args = parser.parse_args()

    data_folder_path = os.path.join(CURRENT_FOLDER_NAME, '..', constants.DATA_FOLDER_NAME, args.type)
    files = [str(file) for file in os.listdir(data_folder_path) if str(file).endswith('csv')]

    output_save_folder = os.path.join(CURRENT_FOLDER_NAME, '..', 'output', args.type,
                                      datetime.now().strftime("%B %d %Y %H-%M-%S"))
    make_dir(output_save_folder)

    file_paths = [os.path.join(data_folder_path, file_name) for file_name in files]

    # ----- Start time -----
    st = time.time() 

    revenue_data = [get_sales_information(file_path)
                    for file_path in file_paths]
    
    en = time.time()
    # ----- End time ----- 
    pprint(revenue_data)
    with open("revenue_data.json", "w") as f:
        f.write(json.dumps(revenue_data))
    
    for yearly_data in revenue_data:
        with open(os.path.join(output_save_folder, f'{yearly_data["file_name"]}.json'), 'w') as f:
            f.write(json.dumps(yearly_data))

        plot_sales_data(yearly_revenue=yearly_data['revenue_per_region'], year=yearly_data["file_name"],
                        plot_save_path=os.path.join(output_save_folder, f'{yearly_data["file_name"]}.png'))
    
    print("Overall time taken : {}".format(en-st))

if __name__ == '__main__':
    main()

