
import os, sys

def makefolders():
    path = 'C:\\our_directories'
    x = int(input('number of folders you need: '))
    for i in range (1,x+1):
        os.chdir(path)
        Newfolder = 'hard_drive-' + str(i)
        try:
            if not os.path.exists(Newfolder):
                os.makedirs(Newfolder)
            path2=path+'\\'+Newfolder
            os.chdir(path2)
            for j in range (1-1):
                Newfolder_2='your_folders'+str(j)
                os.makedirs(Newfolder_2)
        except OSError:
            print("Error!")
    print("You created: " + str(x) + ' folders!')


