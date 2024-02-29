import ctypes

class ByteArray(ctypes.Structure):
    _fields_ = [("data", ctypes.POINTER(ctypes.c_char)),
                ("length", ctypes.c_size_t)]

lib = ctypes.CDLL('lib/libsstable_internal.so')


lib.OpenSSTable.argtypes = [ctypes.c_char_p]
lib.OpenSSTable.restype = ctypes.c_void_p

lib.CloseSSTable.argtypes = [ctypes.c_void_p]
lib.CloseSSTable.restype = None

lib.FreeByteArray.argtypes = [ByteArray]
lib.FreeByteArray.restype = None

lib.SSTableGetValue.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.SSTableGetValue.restype = ByteArray

lib.GetMetaData.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.GetMetaData.restype = ByteArray

lib.GetEntryCount.argtypes = [ctypes.c_void_p]
lib.GetEntryCount.restype = ctypes.c_int32

lib.CreateIterator.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
lib.CreateIterator.restype = ctypes.c_void_p

lib.IteratorGetKey.argtypes = [ctypes.c_void_p]
lib.IteratorGetKey.restype = ByteArray

lib.IteratorGetValue.argtypes = [ctypes.c_void_p]
lib.IteratorGetValue.restype = ByteArray

lib.IteratorHasNext.argtypes = [ctypes.c_void_p]
lib.IteratorHasNext.restype = ctypes.c_bool

lib.IteratorNext.argtypes = [ctypes.c_void_p]
lib.IteratorNext.restype = None

lib.DeleteIterator.argtypes = [ctypes.c_void_p]
lib.DeleteIterator.restype = None

class SSTable:
    def __init__(self, path: str):

        self.path = path
        self.handle = lib.OpenSSTable(path.encode('utf-8'))

    def get_handle(self):
        return self.handle

    def get_value(self, key):
        key_bytes = key.encode('utf-8')
        value_bytes = lib.SSTableGetValue(self.handle, key_bytes)
        value = ctypes.string_at(value_bytes.data, value_bytes.length)
        lib.FreeByteArray(value_bytes)
        return value

    def get_metadata(self, key):
        key_bytes = key.encode('utf-8')
        value_bytes = lib.GetMetaData(self.handle, key_bytes)
        value = ctypes.string_at(value_bytes.data, value_bytes.length)
        lib.FreeByteArray(value_bytes)
        return value

    def get_entry_count(self):
        return lib.GetEntryCount(self.handle)


class SSTableIterator:
    def __init__(self, path, start_key="", max_iterations=None):
        self.path = path
        self.start_key = str(start_key)
        self.max_iterations = max_iterations
        self.current_iteration = 0
        self.iterator = None
        self.sstable = None

    def __enter__(self):
        self.sstable = SSTable(self.path).get_handle()
        self.iterator = lib.CreateIterator(self.sstable, self.start_key.encode('utf-8'))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.iterator:
            lib.DeleteIterator(self.iterator)
        if self.sstable:
            del self.sstable
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.max_iterations is not None and self.current_iteration >= self.max_iterations:
            raise StopIteration
        if lib.IteratorHasNext(self.iterator):
            self.current_iteration += 1
            key = self.get_key()
            value = self.get_value()
            lib.IteratorNext(self.iterator)
            return key, value
        else:
            raise StopIteration

    def next(self):
        # Python 2的兼容性方法
        return self.__next__()
    
    def get_key(self):
        ret = lib.IteratorGetKey(self.iterator)
        key = ctypes.string_at(ret.data, ret.length)
        lib.FreeByteArray(ret)
        return key
    
    def get_value(self):
        ret = lib.IteratorGetValue(self.iterator)
        value = ctypes.string_at(ret.data, ret.length)
        lib.FreeByteArray(ret)
        return value


if __name__ == '__main__':
    sstable_path = 'test/data/test.sstable'
    json_path = 'test/data/test.json'
    sstable = SSTable(sstable_path)
    print(sstable.get_entry_count())
    print(sstable.get_value('1'))
    print(sstable.get_metadata('meta_key'))
    import json
    with SSTableIterator(sstable_path) as sfile, open(json_path, 'w') as jfile:
        for k, v in sfile:
            print(k, v)
            jfile.write(json.dumps(v.decode('utf-8')) + '\n')