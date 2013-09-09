import numpy as np
#import time
#from scipy.spatial import KDTree

def condense(training_set,condensed_set):  
    
    result = []
    check = condensed_set
        
    for case in training_set:
        
        min_distance = float("inf")
        
        for example in condensed_set:
            
            distance = np.linalg.norm(case[1:]-example[1:])
            
            if distance < min_distance:
                min_distance = distance
                #min_distance_variable = example[0]
                
                if case[0] != example[0]:
                    array = np.array([case])
                    np.concatenate([condensed_set,array])
                    np.delete(training_set,array)
        
        print condensed_set
    
    while True:
        if np.array_equal(result, check):
            break
        result = condense(training_set,condensed_set)
        
    return result

fname = 'letter-recognition.data'

data = np.loadtxt(fname, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
training_data, test_data, test_response = data[:10,:],data[19990:,:],data[19990:,0]

condensed_data = test_data[:2]
count = 0
x = condense(training_data,condensed_data)
'''for y in x:
    count +=1'''
print x.shape()


#kdtree = KDTree(training_data,leafsize=10)

#print kdtree.query(training_data, 5, 1, 2)

'''start = time.time()
result = classify(training_data,test_data)
print result
end = time.time()
print "It took " + str((end - start)/60) + " minutes"

correct = 0

for x in xrange(len(test_response)):
    if result[x] == test_response[x]:
        correct += 1

print str(correct) + " test cases classified correctly out of " + str(len(test_response)) + " with an efficiency of " + str(float((correct*100))/len(test_response))''' 