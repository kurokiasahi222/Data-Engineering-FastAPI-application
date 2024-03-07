# Comparing Run Time
### All times are in seconds

### cpu information
'''
cpu_count = 7 == number of files to analyze
'''
## Week 1: Run Time
| Data set      | w1            |           
| ------------- | ------------- |
| Small         | 44.46         |
| Big           | 317.26        |

## Week 2: Run time (average of 5 runs)
### Check results.csv and analyze.ipynb for more info
| Data set      | 1 (same as w1)| 2             | 4             | 7             |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Small         | 46.12         | 31.22         | 21.61         | 16.47         |
| Big           | 299.69        | 213.29        | 139.51        | 122.14        |



# Run tests with prints 
```
PYTHONPATH=../ pytest test.py -s
```

# Run tests without prints 
```
PYTHONPATH=../ pytest test.py
```

# Run the data processing code
````
# Run on `test` data
PYTHONPATH=../ python main.py --type tst

# Run on `small` data
PYTHONPATH=../ python main.py --type sml

# Run on the `big` data
PYTHONPATH=../ python main.py --type bg
````

# Start FastAPI server
````
PYTHONPATH=.. uvicorn server:app --workers 2
````