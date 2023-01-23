import glob
import subprocess

rootdir = 'Q:\VRChat Projects\OSC\TTSVoiceWizard'
searchPattern = 'TTSVoiceWizard-v*.*.*-x86'
programName = 'TTSVoiceWizard.exe'

searchQuery = rootdir + '\\' + searchPattern
searchResults = glob.glob(searchQuery)

latestVersion = searchResults.pop()

# for searchResult in searchResults:
#     print(searchResult)
# print('Latest version is: ' + latestVersion)

# this is garbage and I should feel bad, but it works so whatever
pathToProgram = '"' + latestVersion + '\\' + programName + '"'

subprocess.Popen(pathToProgram)
