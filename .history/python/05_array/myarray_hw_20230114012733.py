# 建立class
class myArray:

# 初始化：data(空列表)，capacity：长度
    def __init__(self, capacity=None):
        self.data = []
        self.capacity = capacity

# getitem：根据索引返回key
    def __getItem__(self, index: int):
        return self.data[index]

# setitem：写入索引和key
    def __setItem__(self, index: int, key: int):
        self.data[index] = key
        return self.data

# len：返回长度
    def __len__(self):
        return len(self.data)

# iter：遍历array
    def __iter__(self):
        for item in self.data:
            yield item

# find：try/except，根据index返回key，object
    def find(self, index: int) -> object:
        try:
            return self.data[index]
        except IndexError:
            return None

# delete：try/except，根据index删除key，bool
    def delete(self, index: int) -> bool:
        try:
            self.data.pop(index)
            return True
        except IndexError:
            return False

# insert: 检查长度，超过则返回false，没有则insert
    def insert(self, index: int, value: int):
        if len(self.data) >= self.capacity:
            return 

# print_all：输出列表