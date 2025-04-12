from json import loads

class FetchExternal:
    def __init__(self, meta) -> None:
        self.meta = meta
    
    def show_meta(self):
        with open(self.meta, 'r') as fp:
            return fp.read()
        
    def get_meta_key(self, key: tuple):
        meta_file = loads(self.show_meta())    
        
        if len(key) > 1:
            meta_value = ""
            for index, k in enumerate(key):
                if index == 0:
                    meta_value = meta_file[k]
                else:
                    meta_value = meta_value[k]
                    
            return meta_value 
                
        elif len(key) == 1:
            return meta_file.get({key[0]})
