import numpy as np
import time
from scipy.spatial import KDTree

def classify(tree,test_set):  
        
        result = []
        
        for case in test_set:
            
            '''min_distance = float("inf")
            
            for example in training_set:
                
                distance = np.linalg.norm(case[1:]-example[1:])
                
                if distance < min_distance:
                    min_distance = distance
                    min_distance_variable = example[0]
            
            test_result = min_distance_variable    
            result.append(chr(int(test_result)+65))'''
            
            tree_value = tree.query(case,1,1.0,2,10.0)
            point = tree_value[1]                

            result.append(point)
            
        return result

fname = 'letter-recognition.data'

data = np.loadtxt(fname, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
training_data, test_data, test_response = data[:15000,:],data[15000:,:],data[15000:,0]
kdtree = KDTree(training_data)

start = time.time()
#values = kdtree.query(test_data, 1, 1.0, 2, 10.0)
points = classify(kdtree,test_data)

result = []

for value in points:
    result.append(chr(int(training_data[value][0])+65))

print result
end = time.time()
print "It took " + str(end - start) + " seconds"

correct = 0

for x in xrange(len(test_response)):
    if result[x] == chr(int(test_response[x])+65):
        correct += 1

print str(correct) + " test cases classified correctly out of " + str(len(test_response)) + " with an efficiency of " + str(float((correct*100))/len(test_response)) 