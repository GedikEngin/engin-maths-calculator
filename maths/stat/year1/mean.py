
total = 0
data_count = int(input('How many elements are there in the dataset:\t'))

for i in range(data_count):
    data_entry = float(input('Please enter the element:\t'))
    total += data_entry

result = total/data_count
print(result, 'is the mean')