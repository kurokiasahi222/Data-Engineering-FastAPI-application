from typing import List, Generator
class DataReader:
    def __init__(self, fp: str, sep: str, col_names: List) -> None:
        self._fp = fp
        self._sep = sep
        self._col_names = col_names

    def __iter__(self) -> Generator:
        """
        Input : None
        Output : Generator

        This method should return an iterable generator. Upon iteration the data should be of type Dict
        For example if the file format is as below:

        StockCode    , Description    , UnitPrice  , Quantity, TotalPrice , Country
        22180        , RETROSPOT LAMP , 19.96      , 4       , 79.84      , Russia
        23017        , APOTHECARY JAR , 24.96      , 1       , 24.96      , Germany

        The generator function should return the rows in the below format:
        {
            'StockCode': '22180',
            'Description': 'RETROSPOT LAMP',
            'UnitPrice': 19.96,
            'Quantity': 4,
            'TotalPrice': 79.84,
            'Country': 'Russia',
        }
        """
        ######################################## YOUR CODE HERE ##################################################
        # output generator -- use 'yield' keyword
        # generate each row: dictionary comprehension

        for n_row, row in enumerate(open(self._fp, "r")):
            row_vals: List = row.strip("\n").split(self._sep)
            # ignore the first line since it is the column names
            # if (n_row) == 0:
            #     continue

            # print(row_vals)
            # define the row_vals dictionary
            row_dict: Dict = {self._col_names[i]: val for i, val in enumerate(row_vals)}

            # return results:
            yield row_dict

    ######################################## YOUR CODE HERE ##################################################

    def get_file_path(self):
        return self._fp

    def get_column_names(self):
        return self._col_names
