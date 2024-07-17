#!/bin/bash

# -- test --
# python main.py --type tst 3
# python main.py --type tst 4

# # Define the array of types
types=("sml" "bg")

# Define the array of n_processes
n_processes=(1 2 4 7) 

# Loop through each type
for i in 1 2 3 4; do
  for type in "${types[@]}"; do
    # Loop through each n_process
    for n in "${n_processes[@]}"; do
      # Execute the Python script with the current combination of type and n_process
      python main.py --type $type $n
    done
  done
done



# chmod +x run_combinations.sh
# ./run_combinations.sh
