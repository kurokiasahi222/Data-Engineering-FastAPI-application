import os
import argparse
import datetime
import json
from global_utils import make_dir, plot_sales_data
from DP import get_sales_information
import constants as constants

CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = argparse.ArgumentParser(
        description="Choose from one of these : [tst|sml|bg]"
    )
    parser.add_argument(
        "--type",
        default="tst",
        choices=["tst", "sml", "bg"],
        help="Type of data to generate",
    )
    args = parser.parse_args()

    data_folder_path = os.path.join(
        CURRENT_FOLDER_NAME, "..", constants.DATA_FOLDER_NAME, args.type
    )
    files = [
        str(file) for file in os.listdir(data_folder_path) if str(file).endswith("csv")
    ]

    output_save_folder = os.path.join(
        CURRENT_FOLDER_NAME,
        "..",
        "output",
        args.type,
        datetime.datetime.now().strftime("%B %d %Y %H-%M-%S"),
    )
    make_dir(output_save_folder)

    file_paths = [os.path.join(data_folder_path, file_name) for file_name in files]
    revenue_data = [get_sales_information(file_path) for file_path in file_paths]
    '''
    When get_sales_information is called it will initialize DP object and
    dp will call describe method. Describe method will insert data into sqlite
    '''
    for yearly_data in revenue_data:
        with open(
            os.path.join(output_save_folder, f'{yearly_data["file_name"]}.json'), "w"
        ) as f:
            f.write(json.dumps(yearly_data))

        plot_sales_data(
            yearly_revenue=yearly_data["revenue_per_region"],
            year=yearly_data["file_name"],
            plot_save_path=os.path.join(
                output_save_folder, f'{yearly_data["file_name"]}.png'
            ),
        )


if __name__ == "__main__":
    main()
