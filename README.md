# Python FastAPI application
This repo contains the work I have completed through <a href="https://uplimit.com/course/intermediate-python">Uplimit's Intermediate python</a>.
Course taught by <a href="https://www.linkedin.com/in/pyemma/">Yang Pei</a> and <a href="https://www.linkedin.com/in/wendyranwei/">Wendy Ran Wei</a>. 

![Screenshot 2024-07-17 at 14 22 55](https://github.com/user-attachments/assets/53693d12-d2db-4389-9b22-249b2169e439)

### Frameworks and APIs Learned:
Throughout the course, I have gained proficiency in serveral frameworks and APIs, including: 
- __FastAPI__: Used to build web applications. 
- __Logging__: Python built-in module for debugging.
- __Profile__: Module to measuring code performance. 
- __Multiprocessing and multi-threading__: Techniques for optimizing code performance.
- __SQL Integration__: Integrated the web applications with SQLite.
- __Advanced Python Concepts__: Generators, comprehensions, and higher-order functions for writing efficient, reusable, and maintainable code.

###  Project: Data Engineer Role at Bamazon
Setting the scene... </br>
You've recently accepted a new role as a Data Engineer at bamazon.com Inc., an e-commerce company based in Dallas. In this role, you'll be a member of the team responsible for building systems that collect, manage, and convert raw data into usable information for data scientists and business analysts.

### Project details: 
1. Data Processing Module: Developed using generators, comprehensions, and object-oriented programming (OOP) principles.
2. Code Optimization: Utilized Python’s multiprocessing module to optimize the performance of the data processing engine.
3. FastAPI Server: Created a FastAPI server to track and monitor the progress of data tasks.
4. Logging: Implemented multiple log configurations using Python's logging module to enhance monitoring and debugging capabilities.

## To follow the code on this repo:
### 1. Install all dependencies
- Make you're using Python version >= 3.9.0
- Install all the modules
```
pip install -r requrirements.txt
```

### 2. Generate data: (Must run this to run the program)
Generate test data (useful for unit testing code)
```
python generate_data.py --type tst
```
Generate small data (useful for quick testing of logic)
```
python generate_data.py --type sml
```
Generate big data (actual data)
```
python generate_data.py --type bg
```

### Run tests with prints 
```
PYTHONPATH=../ pytest test.py -s
```

### Run tests without prints 
```
PYTHONPATH=../ pytest test.py
```

### Run the data processing code
````
# Run on `test` data
PYTHONPATH=../ python main.py --type tst

# Run on `small` data
PYTHONPATH=../ python main.py --type sml

# Run on the `big` data
PYTHONPATH=../ python main.py --type bg
````

### Start FastAPI server
````
PYTHONPATH=.. uvicorn server:app --workers 2
````
or
````
fastapi run server.py
````
### Thanks you to all the Course Staff.
Thank you so much to Yang Pei, Wendy Ran Wei, and other Uplimit's staff member for making this awesome course. 
