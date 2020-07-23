import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self,filename):
        self.file_open = open(filename, 'w')
    @abc.abstractmethod
    def write(self,to_write):
        return

class LogFile(WriteFile):
    def __init__(self,filename):
       super(LogFile,self).__init__(filename)
    def write(self,to_write):
        dt_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        self.file_open.write(dt_str + '       ' + to_write + '\n')
class DelimFile(WriteFile):
    def __init__(self,filename,delimiter):
        self.delimiter = delimiter
        super(DelimFile, self).__init__(filename)
    def write(self,to_write):
        str_to_write = ''
        for element in to_write:
            if ',' in element:
                element = '"' + element + '"'
            str_to_write += element
            str_to_write += self.delimiter
        self.file_open.write(str_to_write + '\n')


log = LogFile('log.txt')
myDelim = DelimFile('delim.csv',',')

log.write('this is a log message')
log.write('this is another log message')

myDelim.write(['a,b','b','c,d','d'])
myDelim.write(['1','2','3','4'])









