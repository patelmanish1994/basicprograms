import os, sys

# Open a file
#provide the path of the directoryin string format

path = "B:"

#this will return he list of files in the directory
directory = os.listdir( path )



#this is the way to print the element of list line by line

#here files is the variable randomly it can be x,y anything

for files in directory: # This would print all the files in directories in seprate lines

   print files
   
   
