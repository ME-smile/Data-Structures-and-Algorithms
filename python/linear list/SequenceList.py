class SeqList:

    def __init__(self,max):
        self.max=max  #max参数表示顺序表的容量
        self.length=0  #默认表长初始化为0
        sefl.data=[None]*self.max  #定义列表，列表元素默认为None，长度为max

    def is_empty(self): #判断是否为空表
        return self.length is 0

    def is_full(self):  #判断是否该表是不是已满
        return self.length is self.max 

    def __getItem__(self,pos):  ##根据下标获取元素
        #对pos的数据类型进行判断
        if not isinstance(pos,int):
            raise TypeError
        else:
            if 0 <= pos < self.max:
                return self.data[pos]
            else:
                return IndexError

    def retrieve(self,item):    ##根据值获取元素
        for i in range(0,self.length):
            if  self.data[i] == item:
                return i
            else:
                return -1



    def __setItem__(self,pos,item): ##根据下标设置元素
        if not isinstance(pos,int):
            raise TypeError
        else:
            if 0 <= pos < self.max:
                  self.data[pos] = item
            else:
                return IndexError

    def __len__(self):  ##获取表长
        return self.length

    def insert(self,pos,item):  ##插入元素,其实，这并不是真正的插入，只是覆盖了原先的None值
        if not pos isinstance(pos,int):
            raise TypeError
        else:
            if is_full():
                return 'SEQLIST IS FULL'
            else:
                if 0 <= pos < self.length:
                    for i in range(self.length,pos,-1):
                         self.data[i]= self.data[i-1]
                     self.data[pos] = item
                    self.length += 1
                else:
                    raise IndexError

    def remove(self,pos):
        if not pos isinstance(pos,int):
            raise TypeError
        else:
            if is_empty():
                return 'SEQLIST IS EMPTY'
            else:
                if 0 <= pos < self.length:
                    for i in range(pos,self.length):
                         self.data[i] = data[i + 1]
                    self.length -= 1

    def append(self,item):
        if is_full():
            return 'SEQLIST IS FULL'
        else:
            self.data[self.length]=item
            self.length + = 1


    def destory(self):
        self.__init__()

    # def display(self):
    #     result

sl=SeqList()
sl.append('ME')








