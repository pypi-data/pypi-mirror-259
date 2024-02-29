import ctypes

lib = ctypes.CDLL('lib/libsstable_internal.so')

lib.CreateSSTableBuilder.argtypes = [ctypes.c_char_p]
lib.CreateSSTableBuilder.restype = ctypes.c_void_p

lib.SetKV.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
lib.SetKV.restype = None

lib.SetMetaData.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
lib.SetMetaData.restype = None

lib.BuildSSTable.argtypes = [ctypes.c_void_p]
lib.BuildSSTable.restype = None

class SSTableBuilder:
    def __init__(self, path: str):
        self.builder = lib.CreateSSTableBuilder(path.encode('utf-8'))
        
    def set_kv(self, key, value):
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(value, str):
            value = value.encode('utf-8')
        lib.SetKV(self.builder, key, value)
            
    def set_metadata(self, key: str, value: str):
        lib.SetMetaData(self.builder, key.encode('utf-8'), value.encode('utf-8'))    
       
    def build(self):
        lib.BuildSSTable(self.builder)
        
if __name__ == '__main__':
    builder = SSTableBuilder('test/data/test.sstable')
    builder.set_kv('key1', '{"name": "Alice", "age": 25}')
    builder.set_kv('key2', 'value2')
    builder.set_metadata('meta1', 'value1')
    builder.set_metadata('meta2', 'value2')
    builder.build()

