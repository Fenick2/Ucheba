# Iterating through the dictionary itself
for x in job2:
    print(x) # prints the keys of job2
    
# Using keys()
for key in job2.keys():
    print(key) # prints the keys of job2
    
# Using values()
for val in job2.values():
    print(val) # prints the values of job2
    
# Dictionary iteration use case
import csv
with open('jobs.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for job in reader:
        
        # Using items()
        for key,val in job.items():
            # Apply any additional processing
            print(key, val) #print the keys and values of each job