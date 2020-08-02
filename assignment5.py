import pickle
import sys
import os


class ConfigFile3(dict):

    def __init__(self, config_name):
        self.config_dir = "configuration_dir"
        self.config_name = config_name
        self.complete_path = self.config_dir + '/{0}'.format(self.config_name)
        empty_dict = {}
        if not os.path.isfile(self.complete_path):
            with open(self.complete_path,'wb') as fh:        #create file
                pickle.dump(empty_dict,fh)
        else:
            with open(self.complete_path,'rb') as fh:
                dict_obj = pickle.load(fh)
                self.update(dict_obj)

    def __setitem__(self, key, value):
        #call the parent's setitem method
        dict.__setitem__(self,key,value)
        #open config file for writing
        with open(self.complete_path,'wb') as fh:
            pickle.dump(dict(self),fh)

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
cd = ConfigFile3('config_file2.pkl')

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

