class ConfigFile(dict):
    def __init__(self,filename):
        self.filename = filename
        #open file for reading
        self.file = open(self.filename,'r')

        lines = self.file.readlines()
        for line in lines:
            # get key and value from file
            key_and_value = line.split('=')
            key = key_and_value[0]
            value = key_and_value[1]
            #write to the dictionary
            dict.__setitem__(self,key,value)

    def __setitem__(self, key, value):
        #call the parent's setitem method
        dict.__setitem__(self,key,value)
        #open config file for writing
        self.file = open(self.filename,'a')
        #write key/value pair
        self.file.write(key + '=' + value + '\n')
        #close the file
        self.file.close()
