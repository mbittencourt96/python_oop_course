import os
import sys

class ConfigFile2(dict):
    def __init__(self, filename):
        self.filename = filename
        try:
            if not os.path.isfile(self.filename):
                file = open(self.filename,'w')    #create file
                file.close()
            else:
                file = open(self.filename,'r')
                for line in file:
                    # get key and value from file
                    line = line.rstrip()
                    key, value = line.split('=',1)
                    # write to the dictionary
                    dict.__setitem__(self, key, value)
        except IOError:
            print('Invalid path!')
            sys.exit()

    def __setitem__(self, key, value):
        #call the parent's setitem method
        dict.__setitem__(self,key,value)
        #open config file for writing
        file = open(self.filename,'w')
        #write key/value pair
        for key,value in self.items():
            file.write("{0}={1}\n".format(key,value))
        #close the file
        file.close()

    def __getitem__(self, key):
        if not key in self:
            raise ConfigKeyError(self,key)
        return dict.__getitem__(self,key)

class ConfigKeyError(Exception):
    def __init__(self,config_file,key):
        self.config_file = config_file     #the ConfigDict instance
        self.key = key      #the key that was requested

    def __str__(self):
        return 'Key "{0}" not found. Available keys: {1}'.format(self.key,list(self.config_file.keys()))


# Test script for the classes above
cd = ConfigFile2('config_file2.txt')

# if 2 arguments on the command line,
# set a key and value in the object's dictionary
if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))
    cd[key] = value

# if 1 argument on the command line, treat it as a key and show the value
elif len(sys.argv) == 2:
    print('reading a value')
    key = sys.argv[1]
    print('the value for {0} is {1}'.format(sys.argv[1], cd[key]))

# if no arguments on the command line, show all keys and values
else:
    print('keys/values:')
    for key in cd.keys():
        print('   {0} = {1}'.format(key, cd[key]))

