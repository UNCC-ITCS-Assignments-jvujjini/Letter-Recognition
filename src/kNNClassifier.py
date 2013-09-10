import numpy as np
import time
from collections import Counter

def classify(training_set,test_set,k):  
        
        result = []
        
        for case in test_set:
            
            k_neighbors = []
            points = []
            min_distance = float("inf")
            
            for example in training_set:
                
                distance = np.linalg.norm(case[1:]-example[1:])
                
                if(len(k_neighbors) < k):
                    k_neighbors.append((distance,example[0]))
                    k_neighbors.sort()
                else:
                    if distance < min_distance:
                        k_neighbors.remove(k_neighbors[-1])
                        k_neighbors.append((distance,example[0]))
                        k_neighbors.sort()
                        min_distance = k_neighbors[-1][0]
                
            for point in k_neighbors:
                    points.append(point[1])
            
            
            nearest_neighbor = Counter(points).most_common(1)
            result.append(chr(int(nearest_neighbor[0][0])+65))
            
        return result

fname = 'letter-recognition.data'

data = np.loadtxt(fname, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
training_data, test_data, test_response = data[:15000,:],data[15000:,:],data[15000:,0]

start = time.time()
result = classify(training_data,test_data,7)
print result
end = time.time()
print "It took " + str((end - start)/60) + " minutes"

correct = 0

for x in xrange(len(test_response)):
    if result[x] == chr(int(test_response[x])+65):
        correct += 1

print str(correct) + " test cases classified correctly out of " + str(len(test_response)) + " with an efficiency of " + str(float((correct*100))/len(test_response)) 