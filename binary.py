import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries)
print(countries[1])
print(countries)



low = 0
high = len(countries) -1
mid = length//2
print(mid)
print("Please enter a country:")
user_input = input ()
value = user_input


while (low <= high ) :
    mid = (low + high)//2
    if (countries[mid] > value):
        high = mid - 1
    elif (countries[mid] < value):
        low = mid + 1
    else:
        print (mid)
        break
