#input function python
import os
#cwd = os.getcwd()
#print (cwd)
def inputs(file_name):
    cwd = os.getcwd()
    rides = []
    #print(cwd)

    F = open(cwd+"/input/"+file_name,'r')
    conditions_ = F.readline()
    conditions = conditions_.rstrip('\n')

    for line in F:
        rides.append(line.rstrip('\n'))

    return conditions, rides

#def outputs()
