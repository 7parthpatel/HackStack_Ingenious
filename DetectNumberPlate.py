import os
from multiprocessing import Process

def check_count(folder_name):
	count_query = 'hadoop fs -ls '+folder_name
	count_query = count_query.split(' ')
	count_output = subprocess.check_output(count_query)	
	if count_output != '':
		count_output = count_output.split('\n')
		count = int(count_output[0].split(' ')[1])
		#print count
		return count,count_output
	else:
		check_count(folder_name)

def filename(count,count_output,fileread_count,folder_name):
	file_name = '/'+count_output[fileread_count+1].split('/',1)[1]
	print file_name
	if '.tmp' not in file_name:
		#call pig file
		pig_command = 'pig -param file='+file_name+' -f Desktop/tweet.pig'
		pig_command = pig_command.split(' ')
		subprocess.call(pig_command)
	#call pig file
		fileread_count = fileread_count + 1
	
	#print fileread_count
	#print folder_name
	while(1):	
		count,count_output = check_count(folder_name)
		if fileread_count < count:
	 		fileread_count = filename(count,count_output,fileread_count,folder_name)

	
def main():
	folder_query = 'hadoop fs -ls /flume'.split(' ')
	folder_output = subprocess.check_output(folder_query)
	folder_output = folder_output.split('\n')
	folder_name = '/'+folder_output[-2].split('/',1)[1]
	print folder_name
	count,count_output = check_count(folder_name)
	fileread_count = 0
	fileread_count = filename(count,count_output,fileread_count,folder_name)
	
if __name__ == '__main__':
    main()

