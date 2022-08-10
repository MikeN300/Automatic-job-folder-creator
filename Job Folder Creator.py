import os
import time

while loopBack == True:
	print('Which Server would you like to store this on? (1) Dunk (2) Funk')
	#Defines variables for Funk or Dunk
	whichServer = input()
		if whichServer == 1:
			path = '/Volumes/Dunk'
			serverIP = 'afp://192.168.3.95'
			shareName = 'OpenJobs'
		elif whichServer == 2
			path = '/Volumes/Funk'
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
				return #Will this return to elif statment?
			elif tryAgain == 2:
				exit
			else
				print('Invalid Selection')
	print('Server mounted!')

	#Defines variables to create folders
	print 'Enter Client Code (Enter it exactly as shown in the ' + shareName + ' folder):'
	clientCode = input()
	#Add code to check if Client Code folder exists on server, if not ask user if they want to os.mkdir)
	print 'Enter Job Number:'
	jobNumber = input()
	print 'Enter Job Name:'
	jobName = input()
	print('Creating folders...')

	#Function to creat folders
	def makeFolders(folderName)
		os.mkdir(path + '/' + clientCode + '/' + jobNumber + ' ' +  jobName + '/' jobNumber + '_' + folderName, mode = Oo777)

	os.mkdir(path + '/' + clientCode + '/' + jobNumber +  jobName)
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
		loopBack = False
		break
	else
			print ('error: invalid selection, please enter "y" or "n"')