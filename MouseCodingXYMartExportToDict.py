#usr/bin/env python

from functools import reduce
import time

def fileToString(filename: str):
    with open(filename) as f:   # open file
        rawContents = f.read()  # read into single string
    return rawContents          # return

def itemToDictAndKey(item: str):
    result = {}                 # create empty dict
    item = item.split("\n")     # split string into seperate lines (one title line and x lines containing parts of the sequence)
    title = item[0]             # assign the title line to it's own variable
    sequence = item[1:]         # assign sequence lines to it's own variable
    title = title.split("|")    # split the title line into a list of ID, Chromosome, Begin, End
    result["chromosome"] = title[1] # put into dict
    result["begin"] = title[2]      # and again
    result["end"] = title[3]        # and again
    result["sequence"] = str(reduce(lambda x, y: x+y, sequence)) # and again after sticking the sequence together into one string. (How this version of reduce works: [1, 2, 3, 4, 5]  -> ((((1+2)+3)+4)+5)
    return title[0], result # return the ID and the Dict that belongs to the ID

def itemsToDict(items: list):
    items = map(lambda x: itemToDictAndKey(x), items) # world's fastest for loop
    #items = [itemToDictAndKey(item) for item in items] #world's second fastest, but easier to read for loop
    return {key: value for (key, value) in items} # convert list into dict and return

if __name__ == "__main__":
    startTime = time.time()
    rawString = fileToString("Mouse_coding_X_Y_mart_export.txt") # put entire file into single string
    items = rawString.split(">")[1:] # split strings using the > that's at the start of every new title and dump the first one since it's always gonna be empty
    resultingDictionary = itemsToDict(items) # convert raw string into dict
    print(resultingDictionary) # bask in the glory of your dicts inside a dict
    print("runtime: %s seconds" % (time.time()- startTime))
    input('Press ENTER to exit')