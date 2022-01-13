from webbot import Browser
import os
import zipfile
import time

def run(email,passwort,path,url,Vorlesungen):

    # open Browser to url
    web = Browser(showWindow=True, downloadPath=path)
    web.maximize_window()
    web.go_to(url)

    # log in
    web.click(id = 'user_idp_iddtext')
    web.click('Universität Basel')
    web.click('Login')
    web.type(email)
    web.type(passwort , into='Password')
    web.click('Anmelden')
    web.click("Herbstsemester")

    # press download buttons
    preString = "bl_cb_"
    for x in range(len(Vorlesungen)):
        if web.exists(Vorlesungen[x]):
            web.click(Vorlesungen[x])
        else:
            continue
        web.click('Aktionen')
        web.click('Mehrere Objekte herunterladen')
        for i in range(6):
            if web.exists(id=preString+str(i)):
                web.click(id=preString+str(i))
        
        web.click('Herunterladen')
        web.go_back()
        web.go_back()
        web.click("Herbstsemester")
    time.sleep(30) #TODO: add wait till finished


    # unzip to folder
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            filedir = path+'/'+file[0:len(file) - 3]
            os.makedirs(filedir)
            for names in zip_file.namelist():
                zip_file.extract(names,filedir) #TODO: Extract only needed files
            zip_file.close()

    #deletes zip files
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            os.remove(filePath) 
