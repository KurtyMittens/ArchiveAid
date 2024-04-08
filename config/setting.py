# File = fileinput.input("config/settings.txt")
import os
class Recent:
    def __init__(self):
        self.filesave = []
        with open("config/recent.conf", 'r') as file:
            for i in file:
                if i[0] != '#' and i[0] != '\n' and i[0] != ' ':
                        file = i.strip()
                        self.filesave.append(file.split("-"))

    def get_filepath(self):
         return self.filesave[1:]
    
    def get_sourcepath(self):
         return self.filesave[0]
    
class Files_extensions:
        def __init__(self) -> None:
            self.file_ext = {
                "Audio":['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'],
                "Compressed":['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
                "Disc":['.bin', '.dmg', '.iso', '.toast', '.vcd'],
                "Data/Database":['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'],
                "Email":['.email', '.eml', '.emlx', '.msg', '.oft', 'ost', '.pst', '.vcf'],
                "Executable":['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.py', '.wsf'],
                "Fonts/file":['.fnt', '.fon', '.otf', '.ttf'],
                "Images":['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.webp'],
                "InternetFiles":['.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php', '.py', '.rss', '.xhtml'],
                "Presentation":['.key', '.odp', '.pps', '.ppt', '.pptx'],
                "Programming":['.c', '.cgi', '.pl', '.class', '.cpp', '.cs', '.h', '.java', '.php', '.py', '.sh', '.swift', '.vb'],
                "Spreadsheets":['.ods', '.xls' '.xlsm', 'xlsx'],
                "System":['.bak','.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp'],
                "Video":['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.webm', '.wmv'],
                "WordProcess":['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd']
            }

        def get_class_ext(self):
             return self.file_ext.keys()
     