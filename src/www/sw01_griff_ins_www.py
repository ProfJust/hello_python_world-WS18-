### Griff ins WWW
### Willemer Kap 17.4
import urllib
website = urllib.urlopen("http://www.willemer.de")
datei = open("kopie.htm", "w")
zeile = "irgendwas"
while zeile:
    zeile = website.readline()
    datei.write(zeile)
website.close()
datei.close()
