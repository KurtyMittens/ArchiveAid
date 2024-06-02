class Recent:
    """returns the data written in the config file"""
    def __init__(self):
        self.filesave = []
        with open("ArchiveAid/config/recent.conf", 'r') as file:
            for i in file:
                if i[0] != '#' and i[0] != '\n' and i[0] != ' ':
                    files = i.strip()
                    self.filesave.append(files.split("-"))
            file.close()

    def get_filepath(self):
        """returns the file paths from the config"""
        return self.filesave[1:]

    def get_sourcepath(self):
        """returns the source path from the config"""
        try:
            return self.filesave[0]
        except IndexError:
            return 1


class SaveRecent:
    """Save the current config to config file"""
    def __init__(self, src, filepath, file_cat, file_path, file_ext):
        """Gets all the directories, extensions (raw and categorized)"""
        self.saved = [src.strip()+'\n']
        for i in zip(filepath, file_cat):
            self.saved.append(i[0] + '-' + i[1] + '\n')

        for j in zip(file_path, file_ext):
            self.saved.append(j[0] + '-' + j[1] + '\n')

    def save_config(self):
        """Save it to the config"""
        with open('ArchiveAid/config/recent.conf', 'w') as save:
            save.write(''.join(self.saved))
            save.close()


class Files_extensions:
    """Provide the list of the categorized extensions that are supported"""
    def __init__(self) -> None:
        self.file_ext = {
            "Audio": ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'],
            "Compressed": ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
            "Disc": ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
            "Data/Database": ['.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'],
            "Email": ['.email', '.eml', '.emlx', '.msg', '.oft', 'ost', '.pst', '.vcf'],
            "Executable": ['.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.exe', '.gadget', '.jar', '.msi', '.wsf'],
            "Fonts/file": ['.fnt', '.fon', '.otf', '.ttf'],
            "Images": ['.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff',
                       '.webp'],
            "InternetFiles": ['.asp', '.aspx', '.cer', '.cfm', '.css', '.htm', '.html', '.js', '.jsp', '.part', '.php',
                              '.rss', '.xhtml'],
            "Presentation": ['.key', '.odp', '.pps', '.ppt', '.pptx'],
            "Programming": ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.py', '.sh', '.swift', '.vb', 'ipnyb'],
            "Spreadsheets": ['.ods', '.xls' '.xlsm', 'xlsx'],
            "System": ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk',
                       '.msi', '.sys', '.tmp'],
            "Video": ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm',
                      '.swf', '.vob', '.webm', '.wmv'],
            "WordProcess": ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wpd']
        }

    def get_class_ext(self):
        """Searching purposes: returns all the class"""
        return self.file_ext.keys()

    def find_support(self, file_ext):
        """Searching purposes: checks if the file extension is supported"""
        for key, values in self.file_ext.items():
            if file_ext in values:
                return key
        return 1
