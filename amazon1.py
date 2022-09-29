import os

## Amazon Parcel Algo
## Main method has user input the number of parcels, store in parcel_count and cut the strips
## Parcel count int input
## For loop for parcel_item by declaring a parcel array and
# using for loop to store in the array by cutting the strips

## Method Explaination
# using set method by using a one line for loop to iterate number of parcels in a day
# and returning the length of the array

def getMinimumDays(parcels):
    parcel_setting = set(x for x in parcels if x>0)
    ## x for x is looping all thru characters
    # and making sure everything is a digit in the int array
    return len(parcel_setting)

if __name__ =='__main__':
    ## Code accepts INTEGER_ARRAY as input
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    parcel_count = int(input().strip())
    parcels = []
    for _ in range(parcel_count):
        parcel_item = int(input().strip())
        # strip removes any uneccesary leading spaces
        parcels.append(parcel_item)
        result = getMinimumDays(parcels)
        fptr.write(str(result)+ '\n')
        fptr.close()