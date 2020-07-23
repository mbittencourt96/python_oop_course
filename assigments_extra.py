import datetime

class WriteFile(object):
    def __init__(self,filename,writer):
        self.writer = writer
        self.writer.open_file(filename)
    def write(self,to_write):
        self.writer.write(to_write)

class LogFile(object):
    def open_file(self,filename):
        self.file_open = open(filename, 'w')
    def write(self,to_write):
        dt_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        self.file_open.write(dt_str + '       ' + to_write + '\n')

class DelimFile(object):
    def __init__(self,delimiter=','):
        self.delimiter = delimiter
    def open_file(self,filename):
        self.file_open = open(filename, 'w')
    def write(self,to_write):
        str_to_write = ''
        for element in to_write:
            if ',' in element:
                element = '"' + element + '"'
            str_to_write += element
            str_to_write += self.delimiter
        self.file_open.write(str_to_write + '\n')

log_file = WriteFile(filename='log.txt',writer=LogFile())
log_file.write('this is a log message')
log_file.write('this is another log message')

csv_file = WriteFile(filename='delim.csv',writer=DelimFile())
csv_file.write(['1','2','3','4'])
csv_file.write(['a','menina','eh','bonita'])