import sys
import csv
import time
import heapq

# Start calculating run time
start_time = time.time()
K = int(sys.argv[1])
pair_counter = 0
with open('males_sorted', 'r') as file1, open('females_sorted', 'r') as file2:
    csv_reader1 = csv.reader(file1)
    csv_reader2 = csv.reader(file2)

    # The dictionary
    ht = {}

    # The min heap
    heap = []

    while True:
        try:
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

            # Update dictionary which has age as key. If current age already exists as a key, then
            # append new id and instance weight to the age. Else, create a new one.
            if int(s1[1]) in ht:
                ht[int(s1[1])].append([int(s1[0]), float(s1[25])])
            else:
                ht[int(s1[1])] = [[int(s1[0]), float(s1[25])]]


        except StopIteration:
            break


    while True:
        try:
            # Reads next entry from males_sorted
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


            # If age already exists in females' dictionary, append in list Q the relevant fields
            # from all the entries with that age
            if int(s2[1]) in ht:
                for lista in ht[int(s2[1])]:

                    # temp_list = instance weight sum, male id , female id
                    temp_list = [float(s2[25]) + lista[1], lista[0], int(s2[0])]

                    if pair_counter < K + 1:
                        # Put them in the heap
                        heapq.heappush(heap, temp_list)
                        pair_counter += 1
                    else:
                        heapq.heappop(heap)
                        heapq.heappush(heap, temp_list)



        except StopIteration:
            break

    result_counter = 0


    # Save K largest results in results list
    results = heapq.nlargest(K, heap, key = lambda record: record[0])


    # Print results
    for i in range(K):
        print(str(result_counter + 1) + '. pair: ' + str(results[result_counter][1]) + ',' + str(results[result_counter][2]) + ' score: ' + str("{:.2f}".format(results[result_counter][0])))
        result_counter += 1


print("\nProgram was executed in: " + str("{:.2f}".format((time.time() - start_time) * 1000)) + " msec")
