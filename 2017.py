from csv import reader
i = 0
# open file in read mode
with open('place_tiles_2017.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the Csv using reader objust
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            print(row[2] + ', ' + row[3])
            i += 1
            #print(row)
print(i)