import os
Print('Which Server would you like to store this on? (1) Dunk (2) Funk')
			if 1 than path = /Volumes/Dunk
			elif 2 than path = /Volumes/Funk
			else print ('error: invalid selection')

if path == '/Volumes/Dunk'
	serverIP = afp://192.168.3.95
elif path == '/Volumes/Funk:'
	serverIP = smb://192.168.3.96

print('Checking if server is connected…')
	try:
		cd path
	except:
		try:
			mount ServerIP
			print('Mounting Server…')
		except:
			print('Error mounting server ' + path + '. Please check your VPN connection and try again')
			print('Would you like to (1) try again, or (2) exit?')
			tryAgain = input()
			if tryAgain == 1 :
				return
			elif tryAgain == 2:
				exit
			else
				print('Invalid Selection')
					(possible “would you like to exit or retry connection?” Dialog here?)

print 'Enter Client Code:'
input(clientCode)
					(Check if Client Code folder exists on server, if not ask user if they want to mkdir)
print 'Enter Job Number:'
input(jobNumber)
print 'Enter Job Name:'
input(jobName)


def makeFolders(folderName)
	mkdir path + '/' + clientCode + '/' + jobNumber + ' ' +  jobName + '/' jobNumber + '_' + folderName

mkdir path + '/' + clientCode + '/' + jobNumber +  jobName
makeFolders(PDF)
makeFolders(SRC)
makeFolders(Layout)
makeFolders(Links)
print('Done creating folders for ' + clientCode + '/' + jobNumber + ' ' +  jobName + ' on ' + path + '!')
wait 3000 exit