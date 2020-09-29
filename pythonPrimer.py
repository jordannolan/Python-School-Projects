# Nolan Jordan 800905892 Python Primer. 9/2/2018
import io
import os

# Read a file and save it as a 2d list of Ints, for loop and if statements are
# to turn the list from strings to integers, this function returns the int list
# Function only handles 1s and 0s more versatility can be added later if needed. 
def openGrid(inFile):
    with open(inFile, 'rU') as in_file:
        List = in_file.read().split(' ')
    for x in range(len(List)):
        if List[x] == '1\n0':
            #List.remove(List[x])
            List[x] = 1
            List.insert(x+1,0)
        elif List[x] == '1\n1':
            #List.remove(List[x])
            List[x] = 1
            List.insert(x+1,1)
        elif List[x] == '0\n0':
            #List.remove(List[x])
            List[x] = 0
            List.insert(x+1,0)
        elif List[x] == '0\n1':
            #List.remove(List[x])
            List[x] = 0
            List.insert(x+1,1)
    for x in range(len(List)):
        List[x] = int(List[x])
    return List

#Write to a text file takes a list parameter,name of the file to be created and
#the width of the grid to set bounds in the new .txt file.
def writeGrid(aList,newfile,width):
    index = 0
    with open(newfile, 'w') as out_file:
        for x in range(len(aList)):
            if index == width:
                out_file.write('\n')
                index = 0
            out_file.write(str(aList[x])+' ')
            index+= 1

# calls to run the program parameters may have to be changed to work with system
# data.
myList = openGrid('practiceGrid.txt')
print(myList)
writeGrid(myList,'output.txt',8)



