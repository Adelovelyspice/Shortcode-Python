import webbrowser as wb 
import os

def workauto():
    codepath = "C:\\ProgramFiles\\Sublime_text.exe"
    os.startfile(codepath)
    chrome_path = 'c:/Users/DELL/Documents/Projects Data Analysis/Python/'Google/chrome/application/chrome.exe %s'
    #URLs = ("stackoverflow.com",
    #       "gmail.com"
    #         "google.com"
    #          "youtube.com"
    #           github/Adelovelyspice")
    # for url in URLS:
    
    url = input("Enter name of the website:-")
wb.get(chrome_path).open(url)

workauto()