class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic={}
        self.capacity=capacity
        

    def get(self, key):
        if key in self.dic:
            temp= self.dic[key]
            del self.dic[key]
            self.dic[key]=temp
            return temp
        return -1
        

    def put(self, key, value):
        if key in self.dic:
            del self.dic[key]
            self.dic[key]=value              
        else:
            self.dic[key]=value
        
        if len(self.dic)> self.capacity:
            del self.dic[next(iter(self.dic.keys()))]
        
