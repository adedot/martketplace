#utils.py
import os

picture_directory = "/Users/adetolaadewodu/pyramid_env/profile_pictures/"

def handle_file_upload(file, newfile):

	print "Creating file ", newfile

	destination = open(newfile, 'wb+')
   	
		#  Write contents to file
	for line in file['fp']:

   		destination.write(line)
    
	destination.close()



	return newfile

def create_file(file_name):
	
	destination = open(file_name, 'rb+')

	data = destination.read()

	return data

