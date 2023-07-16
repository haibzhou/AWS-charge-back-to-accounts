#build subnets source/destination matrix
#each subnet is source, destination is enery other subnets
import json


#open file to write
file_matrix = open("subnets-src-dst-matrix.txt", 'w')
#open file to read
file = open("describe-subnets.txt", 'r')

#file read each line
for line in file:
    file2 = open("describe-subnets.txt", 'r')
    for line2 in file2:  

        if (line != line2) :
            json_data = [{'source': line, 'destination': line2}]
            print(json_data)
            #json_data = json.dumps(json_data)
            #print(json_data)
            
            #strip \n in line
#            line = line.rstrip('\n')
#            source_destination = line +'='+ line2
#            print(source_destination)
#            file_matrix.write(source_destination)
            file_matrix.write(json.dumps(json_data)+'\n')



    file2.close()




#close file
file.close()
file_matrix.close()
