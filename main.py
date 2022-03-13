import GUI
import LoadnZip
import codecs
import os


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#pathData = 'C:\\Users\\edi54\\Documents\\Programmierprojekt\\Python and Shit\\Data.txt'
pathDownload = 'C:/Users/Public/Documents'
url = 'https://adam.unibas.ch/login.php?target=&client_id=adam&cmd=force_login&lang=de'
try:
    # open file and save to lines
    with codecs.open(os.path.join(__location__, 'Data.txt'),'r','utf-8') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
except FileNotFoundError:

    # if first time using or deleted data file
    fiel = codecs.open("Data.txt","w+", "utf-8")
    GUI.logIn(__location__,pathDownload, url)
    with codecs.open(os.path.join(__location__, 'Data.txt'),'r','utf-8') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
if len(lines) >= 4:

    # save data
    email = lines[0]
    passwort = lines[1]
    url = lines[2]
    pathDownload = lines[3]
    amount = int(lines[4])
    LoadnZip.run(email,passwort,pathDownload,url,amount)
else:
    print("Delete Data.txt and try again!")