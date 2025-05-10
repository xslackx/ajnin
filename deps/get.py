from deps import fetch
from zipfile import ZipFile
from os import listdir, getcwd
from urllib.request import urlopen

class PopulateHub:
    def __init__(self, meta, download: bool) -> None:
        if meta == False:
            self.populate(download=download)
            return
        else:
            self.meta = meta
            
    def new_tool(self): pass
    def update_tool(self, tool): pass
    def populate(self, download: bool):
        if download:
            for url in fetch.FetchExternal("configs/external.json").get_meta_key(("tools", "git")):
                try:
                    if urlopen(url):
                        tool_name = url.split('/')[-1].replace(".git", "")
                        with open(f'zips/{tool_name}.zip', 'wb') as new_tool:
                            master = url.replace(".git", "")
                            master = url+"/archive/refs/heads/master.zip"
                            new_tool.write(urlopen(master).read())                    
                except:
                    print({"status": "error", "url": f"{url}"})
        
        zip_files = listdir("zips")
        for file in zip_files:
            full_path = getcwd()+"/zips/"+f"{file}"
            try:
                with ZipFile(full_path, 'r') as tool:
                    tool.extractall(getcwd()+"/hub_tools/")
                    tool.close()
            except:
                print({"status": "error", "zip_file": f"{file}"})