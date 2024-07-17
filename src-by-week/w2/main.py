from utils_w2 import *
import argparse
import json
import csv
import multiprocessing

# CURRENT_FOLDER_NAME = os.path.dirname(os.path.abspath(__file__))

def main() -> List[Dict]:
    """
    Use the `batch_files` method to create batches of files that needs to be run in each process
    Use the `run` method to fetch revenue data for a given batch of files -> actual work is done

    Use multiprocessing module to process batches of data in parallel
    Check `multiprocessing.Pool` and `pool.starmap` methods to help you with the task
    At the end check the overall time taken in this code vs the time taken in W1 code

    :return: Revenue data in the below format

    [{
        'total_revenue': float,
        'revenue_per_region': {
                                'China': float,
                                'France': float,
                                'Germany': float,
                                'India': float,
                                'Italy': float,
                                'Japan': float,
                                'Russia': float,
    
                                'United Kingdom': float,
                                'United States': float},
        'file_name': str
    },{
        'total_revenue': float,
        'revenue_per_region': {
                                'China': float,
                                'France': float,
                                'Germany': float,
                                'India': float,
                                'Italy': float,
                                'Japan': float,
                                'Russia': float,
                                'United Kingdom': float,
                                'United States': float},
        'file_name': str
    },
    ....
    ....
    ....
    ]
    """

    # n_processes = 3 # you may modify this number - check out multiprocessing.cpu_count() as well
    # do not make more processes than cpu count

    # if len(sys.argv < 4):
    #     print("Usage: python main.py --type [choice] [Optional: number of process to use]")

    parser = argparse.ArgumentParser(description="Choose from one of these : [tst|sml|bg]")
    parser.add_argument('--type',
                        default='tst',
                        choices=['tst', 'sml', 'bg'],
                        help='Type of data to generate')
    parser.add_argument("n_processes", type=int, help="number of processes")
    
    args = parser.parse_args()
    n_processes = args.n_processes

    data_folder_path = os.path.join(CURRENT_FOLDER_NAME, '..', src.constants.DATA_FOLDER_NAME, args.type)
    files = [str(file) for file in os.listdir(data_folder_path) if str(file).endswith('csv')]
    output_save_folder = os.path.join(CURRENT_FOLDER_NAME, '..', 'output-w2', args.type,
                                      datetime.now().strftime("%B %d %Y %H-%M-%S"))
    make_dir(output_save_folder)
    file_paths = [os.path.join(data_folder_path, file_name) for file_name in files]
    
    batches, real_n_processes = batch_files(file_paths=file_paths, n_processes=n_processes)

    # ----- Start time ----- 
    st = time.time() 
    with multiprocessing.Pool(processes=real_n_processes) as pool:
        revenue_data = pool.starmap(run, [(batch, i) for i, batch in enumerate(batches)])
        revenue_data = flatten(revenue_data)

        # close the pool
        pool.close()
        pool.join() 
        
    
    en = time.time()
    # ----- End time ----- 
    for yearly_data in revenue_data:
        with open(os.path.join(output_save_folder, f'{yearly_data["file_name"]}.json'), 'w') as f:
            f.write(json.dumps(yearly_data))
        
        plot_sales_data(yearly_revenue=yearly_data["revenue_per_region"], year=yearly_data["file_name"], 
                        plot_save_path=os.path.join(output_save_folder, f'{yearly_data["file_name"]}.png')) 
        

    overall_time = en - st
    print("Overall time taken : {}".format(overall_time))
    rows: List = [real_n_processes, args.type, overall_time]
    with open("results.csv", "a") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(rows)

    # should return revenue data
    return revenue_data

if __name__ == '__main__':
    main()
    # revenue_data = main()
    # pprint(revenue_data)
