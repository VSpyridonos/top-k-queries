import sys
import csv
import time

def top_k_join():
    global is_first_males
    global is_first_females
    global p1_max
    global p2_max
    global p1_cur
    global p2_cur
    global L1
    global L2
    global Q
    global results_list
    global result_counter
    global egkyres_grammes_males
    global egkyres_grammes_females


    # While results list is empty
    while not results_list:

        # Reads next entry from males_sorted
        s1 = next(csv_reader1)


        # Takes first 8 characters from marital_status to check if equals " Married"
        marital_status = s1[8][0] + s1[8][1] + s1[8][2] + s1[8][3] + s1[8][4] + s1[8][5] + s1[8][6] + s1[8][7]

        
        '''
        Check if entry is valid by checking if the person is underage or married. If one of two is true,
        get next entry until there is a valid one. 
        '''
        while int(s1[1]) < 18 or marital_status == " Married":
            s1 = next(csv_reader1)
            marital_status = s1[8][0] + s1[8][1] + s1[8][2] + s1[8][3] + s1[8][4] + s1[8][5] + s1[8][6] + s1[8][7]

            # Check if it's the first entry that has been read. If it is, then p1_max = instance_weight
            if is_first_males == 0:
                # p1_max = instance weight
                p1_max = float(s1[25])


        # Check if it's the first entry that has been read. Checking again in case it's the first 
        # valid entry of the file
        if is_first_males == 0:
            p1_max = float(s1[25])
        is_first_males += 1


        # Increment the valid line counter
        egkyres_grammes_males += 1

        # Update p1_cur
        p1_cur = float(s1[25])

        
        # Update dictionary which has age as key. If current age already exists as a key, then
        # append new id and instance weight to the age. Else, create a new one.
        if int(s1[1]) in L1:
            L1[int(s1[1])].append([int(s1[0]), float(s1[25])])
        else:
            L1[int(s1[1])] = [[int(s1[0]), float(s1[25])]]



        # If age already exists in females' dictionary, append in list Q the relevant fields
        # from all the entries with that age
        if int(s1[1]) in L2:
            for lista in L2[int(s1[1])]:
                # temp_list = male id, female id, average weight
                temp_list = [int(s1[0]), lista[0], (float(s1[25]) + lista[1]) / 2]
                Q.append(temp_list)


        # Calculate threshold T for all the entries except the first one
        if is_first_males != 1:
            T = max(((p1_max + p2_cur) / 2), ((p1_cur + p2_max) / 2))


        # Out of all entries in Q, append to results_list those whose average weight
        # is above threshold T
        for el in Q:
            if el[2] > T:
                results_list.append(el)



        # Reads next entry from females_sorted
        s2 = next(csv_reader2)


        # Takes first 8 characters from marital_status to check if equals " Married"
        marital_status = s2[8][0] + s2[8][1] + s2[8][2] + s2[8][3] + s2[8][4] + s2[8][5] + s2[8][6] + s2[8][7]

        '''
        Check if entry is valid by checking if the person is underage or married. If one of two is true,
        get next entry until there is a valid one. 
        '''
        while int(s2[1]) < 18 or marital_status == " Married":
            s2 = next(csv_reader2)
            marital_status = s2[8][0] + s2[8][1] + s2[8][2] + s2[8][3] + s2[8][4] + s2[8][5] + s2[8][6] + s2[8][7]

            # Check if it's the first entry that has been read. If it is, then p2_max = instance_weight
            if is_first_females == 0:
                # p2_max = instance_weight
                p2_max = float(s2[25])


        # Check if it's the first entry that has been read. Checking again in case it's the first 
        # valid entry of the file
        if is_first_females == 0:
            p1_max = float(s1[25])
        is_first_females += 1

        egkyres_grammes_females += 1

        # Update p2_cur
        p2_cur = float(s2[25])

        # Update dictionary which has age as key. If current age already exists as a key, then
        # append new id and instance weight to the age. Else, create a new one.
        if int(s2[1]) in L2:
            L2[int(s2[1])].append([int(s2[0]), float(s2[25])])
        else:
            L2[int(s2[1])] = [[int(s2[0]), float(s2[25])]]



        # If age already exists in males' dictionary, append in list Q the relevant fields
        # from all the entries with that age
        if int(s2[1]) in L1:
            for lista in L1[int(s2[1])]:
                 # temp_list = male id, female id, average weight
                temp_list = [lista[0], int(s2[0]), (float(s2[25]) + lista[1]) / 2]
                Q.append(temp_list)


        # Calculate threshold T
        T = max(((p1_max + p2_cur) / 2), ((p1_cur + p2_max) / 2))

        # Out of all entries in Q, append to results_list those whose average weight
        # is above threshold T
        for el in Q:
            if el[2] > T:
                results_list.append(el)



    # Sort results_list by entries average weight 
    results_list = sorted(results_list, key = lambda record: record[2])

    # Print the fields of the max element in the list
    print(str(result_counter) + '. pair: ' + str(results_list[0][0]) + ',' + str(results_list[0][1]) + ' score: ' + str("{:.2f}".format(results_list[0][2]*2)))
    Q = []

    # Remove max element from the list
    results_list.pop()
    result_counter += 1
    return




# Start calculating run time
start_time = time.time()
K = int(sys.argv[1])
with open('males_sorted', 'r') as file1, open('females_sorted', 'r') as file2:
    csv_reader1 = csv.reader(file1)
    csv_reader2 = csv.reader(file2)
    p1_max = 0
    p2_max = 0
    p1_cur = 0
    p2_cur = 0
    is_first_males = 0
    is_first_females = 0
    egkyres_grammes_males = 0
    egkyres_grammes_females = 0
    L1 = {}
    L2 = {}
    Q = []
    results_list = []
    result_counter = 1


    # Call function K times
    for i in range(K):
        top_k_join()

print("\nProgram was executed in: " + str("{:.2f}".format((time.time() - start_time) * 1000)) + " msec")
print("Valid lines from males_sorted: " + str(egkyres_grammes_males))
print("Valid lines from apo females_sorted: " + str(egkyres_grammes_females))
