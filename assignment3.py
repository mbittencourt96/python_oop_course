import sys
from ConfigFile import ConfigFile

cd = ConfigFile('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))

    cd[key] = value

else:

    print('reading data')
    for key in cd.keys():
        print('   {0} = {1}'.format(key, cd[key]))
