import os
import sys
from pprint import pprint
from utils import *

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_FOLDER)
# Add parent directory to sys.path if not already included
if PARENT_DIR not in sys.path:
    sys.path.append(PARENT_DIR)
import src.constants as constants
from src.global_utils import blockPrint, enablePrint

def main():
    col_names = [constants.OutDataColNames.STOCK_CODE, constants.OutDataColNames.DESCRIPTION,
                 constants.OutDataColNames.UNIT_PRICE, constants.OutDataColNames.QUANTITY,
                 constants.OutDataColNames.TOTAL_PRICE, constants.OutDataColNames.COUNTRY,
                 constants.OutDataColNames.INVOICE_NO, constants.OutDataColNames.DATE]

    data_reader = DataReader(fp=os.path.join(CURRENT_FOLDER, '..', 'data', 'tst', '2015.csv'), sep=',',
                             col_names=col_names)
    
    data_gen = (row for row in data_reader)
    print(next(data_gen))
    print(next(data_gen))
    print(next(data_gen))


if __name__ == '__main__':
    main()