import numpy as np
import time

def condense(training_set,condensed_set):  
    
    training_set = training_set.tolist()
    condensed_set = condensed_set.tolist()
    counter = True
    
    while(counter):
        counter = False    
        for case in condensed_set:
                
            min_distance = float("inf")
            
            for example in training_set:
                if not counter:
                    distance = np.linalg.norm(np.array(case[1:])-np.array(example[1:]))
                    
                    if distance < min_distance:
                        min_distance = distance
                        min_distance_variable = case[0]
                        correct_variable = example[0]
                        
                        if correct_variable != min_distance_variable:
                            counter = True
                            condensed_set.append(training_set.pop(training_set.index(example)))
        
    return np.array(condensed_set)

def classify(training_set,test_set):  
        
        result = []
        
        for case in test_set:
            
            min_distance = float("inf")
            
            for example in training_set:
                
                distance = np.linalg.norm(case[1:]-example[1:])
                
                if distance < min_distance:
                    min_distance = distance
                    min_distance_variable = example[0]
            
            test_result = min_distance_variable    
            result.append(chr(int(test_result)+65))
            
        return result

fname = 'letter-recognition.data'

data = np.loadtxt(fname, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
training_data, test_data, test_response = data[:15000,:],data[15000:,:],data[15000:,0]

condensed_data = training_data[50:52]
condensed_data = condense(training_data,condensed_data)

start = time.time()
result = classify(training_data,condensed_data)
print result
end = time.time()
print "It took " + str((end - start)/60) + " minutes"

correct = 0

for x in xrange(len(test_response)):
    if result[x] == chr(int(test_response[x])+65):
        correct += 1

print str(correct) + " test cases classified correctly out of " + str(len(test_response)) + " with an efficiency of " + str(float((correct*100))/len(test_response)) 