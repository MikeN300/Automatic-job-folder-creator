import os
import time

while loopBack == True:
	Print('Which Server would you like to store this on? (1) Dunk (2) Funk')
	#Defines variables for Funk or Dunk
	whichServer=input()
		if whichServer == 1:
			path = /Volumes/Dunk
			serverIP = 'afp://192.168.3.95'
			shareName = 'OpenJobs'
		elif whichServer == 2
			path = /Volumes/Funk
			serverIP = 'smb://192.168.3.96'
			shareName = 'Projects'
		else
			print ('error: invalid selection please enter 1 for Dunk or 2 for Funk')

	#Checks server connection and attempts to connect if not available.
	print('Checking if server is connected…')
		
		serverMounted = os.path.exists(path + "/" shareName)
		if serverMounted = True:
			break
		elif serverMounted = False:
			try:
				print('Mounting Server…')
				#mount ServerIP
				serverMounted = True
			except:
				print('Error mounting server ' + path + '. Please check your VPN connection and try again')
				print('Would you like to (1) try again, or (2) exit?')
				tryAgain = input()
				if tryAgain == 1 :
					return #double return? Goto line 17?
				elif tryAgain == 2:
					exit
				else
					print('Invalid Selection')

	#Defines variables to create folders
	print 'Enter Client Code (Enter it exactly as shown in the ' + shareName + ' folder):'
	input(clientCode)
	#Check if Client Code folder exists on server, if not ask user if they want to mkdir)
	print 'Enter Job Number:'
	input(jobNumber)
	print 'Enter Job Name:'
	input(jobName)
	print('Creating folders...')

	#Creates Folders
	def makeFolders(folderName)
		mkdir path + '/' + clientCode + '/' + jobNumber + ' ' +  jobName + '/' jobNumber + '_' + folderName

	mkdir path + '/' + clientCode + '/' + jobNumber +  jobName
	makeFolders(PDF)
	makeFolders(SRC)
	makeFolders(Layout)
	makeFolders(Links)
	print('Done creating folders in ' + clientCode + '/' + jobNumber + ' ' +  jobName + ' on ' + path + '!')

	#Loops back to beginning of program or closes while loop to end.
	print('Would you like to create another job folder? (y or n)')
	createAnotherFolder = input()
	if createAnotherFolder == 'y' OR 'Y' OR 'Yes' #Check OR operator syntax
		loopBack = True
	elif createAnotherFolder == 'n' OR 'N' OR 'No'
		break
	else
			print ('error: invalid selection, please enter "y" or "n"')