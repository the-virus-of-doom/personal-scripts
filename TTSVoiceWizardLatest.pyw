import glob
import os
import subprocess

rootdir = 'Q:\VRChat Projects\OSC\TTSVoiceWizard'
searchPattern = 'TTSVoiceWizard-v*.*.*-x86'
programName = 'TTSVoiceWizard.exe'

searchQuery = rootdir + '\\' + searchPattern
searchResults = glob.glob(searchQuery)

# for searchResult in searchResults:
#     print(searchResult)

latestVersion = searchResults.pop()

# print('Latest version is: ' + latestVersion)

pathToProgram = '"' + latestVersion + '\\' + programName + '"'

# os.system(pathToProgram)
subprocess.Popen(pathToProgram)
