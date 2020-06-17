with open('jobs.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    for job in reader:
        
        # Using sorted() to sort a dictionary's items on the keys
        for key,val in sorted(job.items(),key=lambda item:item[0]):
        
            # Apply any additional processing
            print(key, val) #print the keys and values of each job