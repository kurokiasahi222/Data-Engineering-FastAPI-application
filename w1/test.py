import os
import sys
from main import get_sales_information
from utils import DataReader
from pprint import pprint

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_FOLDER)
# Add parent directory to sys.path if not already included
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)
import constants
from global_utils import blockPrint, enablePrint


def test_data_reader():
    col_names = [constants.OutDataColNames.STOCK_CODE, constants.OutDataColNames.DESCRIPTION,
                 constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.QUANTITY,
                 constants.OutDataColNames.TOTAL_PRICE, constants.OutDataColNames.COUNTRY,
                 constants.OutDataColNames.INVOICE_NO, constants.OutDataColNames.DATE]

    blockPrint()
    data_reader = DataReader(fp=os.path.join(CURRENT_FOLDER, '..', 'data', 'tst', '2015.csv'), sep=',',
                             col_names=col_names)

    data_gen = (row for row in data_reader)
    # skipping column names
    _ = next(data_gen)

    # first row
    row_1 = next(data_gen)
    enablePrint()

    # check if row is a dict
    assert isinstance(row_1, dict)

    # check if the row contains all the required data
    assert all([(col_name in row_1.keys()) for col_name in col_names])

    pprint(row_1)


def test_revenue_per_region():
    blockPrint()
    data_folder_path = os.path.join(CURRENT_FOLDER, '..', constants.DATA_FOLDER_NAME, 'tst')
    files = [str(file) for file in os.listdir(data_folder_path) if str(file).endswith('csv')]

    file_paths = [os.path.join(data_folder_path, file_name) for file_name in files]
    revenue_data = [{'file_path': file_path, 'revenue_data': get_sales_information(file_path)}
                    for file_path in file_paths]
    enablePrint()

    assert len(revenue_data) > 0
    assert all([(True if isinstance(each, dict) else False) for each in revenue_data])
    assert all([len(each) > 0 for each in revenue_data])

    pprint(revenue_data)
