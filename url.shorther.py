import pyshorteners

url = input("Enter your preferred url : \n")

print("URL after shortening :-", pyshorteners.Shortener().tinyurl.short(url))