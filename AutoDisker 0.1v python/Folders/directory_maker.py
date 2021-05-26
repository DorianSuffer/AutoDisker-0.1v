import os, sys

def directory_maker():
    path = 'c:\\'
    for i in range (1,2):
        os.chdir(path)
        Newfolder = 'our_directories'
        try:
            if not os.path.exists(Newfolder):
                os.makedirs(Newfolder)
            path2=path+'\\'+Newfolder
            os.chdir(path2)
            for j in range (1-1):
                Newfolder_2 = 'our_directories_test' + str(j)
                os.makedirs(Newfolder_2)
        except OSError:
            print("Error!")


