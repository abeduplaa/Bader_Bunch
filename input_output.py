#input function python
import os
#cwd = os.getcwd()
#print (cwd)
def inputs(file_name):
    cwd = os.getcwd()
    rides = []
    #print(cwd)

    F = open(cwd+"/input/"+file_name,'r')
    conditions_2 = F.readline()
    conditions_1 = conditions_2.rstrip('\n')
    conditions   = [int(n) for n in conditions_1.split()]
    for line in F:
        line_noend = line.rstrip('\n')
        line_int = [int(n) for n in line_noend.split()]
        rides.append(line_int)

    return conditions, rides

#def outputs()
