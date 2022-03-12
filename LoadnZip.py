from webbot import Browser
import os
import zipfile
import time
import bs4
import lxml.html
from waiting import wait

def downloads_finished(path):
    for file in os.listdir(path):
        if file.endswith(".zip"):
            continue
        else:
            return False
    return True

def run(email,passwort,path,url,amount):
    
    # make dir in path
    path = os.path.join(path, "Vorlesungen")
    os.mkdir(path)
    
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

    # scrape html source code to get lectures
    source = web.get_page_source();
    soup = bs4.BeautifulSoup(source, "html.parser")
    div = soup.find_all("h4", {"class": "il_ContainerItemTitle"})
    content = str(div)
    t = lxml.html.fromstring(content)
    Vorlesungen = t.text_content()[1:].split(", ")
    Vorlesungen = Vorlesungen[:amount]

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

    # wait till all downloads finishfinished
    wait(lambda: downloads_finished(path), timeout_seconds=180, waiting_for="something to be ready")
   

   
    # unzip to folder
    files=os.listdir(path)
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            filedir = path+'/'+file[0:len(file) - 3]
            os.makedirs(filedir)
            for names in zip_file.namelist():
                zip_file.extract(names,filedir)
            zip_file.close()

    #deletes zip files
    for file in files:
        if file.endswith('.zip'):
            filePath=path+'/'+file
            os.remove(filePath)