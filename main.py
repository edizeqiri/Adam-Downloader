import GUI
import LoadnZip
import codecs
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#pathData = 'C:\\Users\\edi54\\Documents\\Programmierprojekt\\Python and Shit\\Data.txt'
pathDownload = 'C:/Users/Public/Documents'

try:
    # open file and save to lines
    with codecs.open(os.path.join(__location__, 'Data.txt'),'r','utf-8') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
except FileNotFoundError:

    # if first time using or deleted data file
    fiel = codecs.open("Data.txt","w+", "utf-8")
    GUI.logIn(__location__,pathDownload)
    with codecs.open(os.path.join(__location__, 'Data.txt'),'r','utf-8') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
if len(lines) >=5:     

    # save data
    email = lines[0]
    passwort = lines[1]
    url = lines[2]
    pathDownload = lines[3]
    Vorlesungen = [None] * (len(lines) - 10)
    for i in range(4,len(lines)):
        Vorlesungen.append(lines[i])
    LoadnZip.run(email,passwort,pathDownload,url,Vorlesungen)
else:
    #TODO: make them repeat above
    print("penis")


