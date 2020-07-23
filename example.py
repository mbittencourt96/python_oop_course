class MaxSizeList(object):
    def __init__(self,maxSize):
        self.list_words = []
        self.maxSize = maxSize
    def push(self,word):
        self.list_words.append(word)
        if (len(self.list_words) > self.maxSize):
            self.list_words.pop(0)
    def get_list(self):
        return self.list_words

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push('hey')
a.push('ho')
a.push('lets')
a.push('go')

b.push('hey')
b.push('ho')
b.push('lets')
b.push('go')

print(a.get_list())
print(b.get_list())
