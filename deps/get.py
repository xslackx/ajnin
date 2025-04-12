from urllib.request import (
    urlopen,
    url2pathname,
    urlretrieve
    )
from html import unescape

class PopulateHub:
    def __init__(self, meta) -> None:
        if meta == False:
            self.populate()
            return
        else:
            self.meta = meta
            
    def new_tool(self): pass
    def update_tool(self, tool): pass
    def populate(self):
        from deps import fetch
        for url in fetch.FetchExternal("external.json").get_meta_key(("tools", "git")):
            try:
                if urlopen(url):
                    tool_name = url.split('/')[-1].replace(".git", "")
                    with open(f'zips/{tool_name}.zip', 'wb') as new_tool:
                        master = url.replace(".git", "")
                        master = url+"/archive/refs/heads/master.zip"
                        new_tool.write(urlopen(master).read())
                    
            except:
                print(f"status: offline, url: {url}")