import numpy as np
from kNNClassifier import kNNClassifier
import time

fname = 'letter-recognition.data'

data = np.loadtxt(fname, np.float32, delimiter=',', converters={ 0 : lambda ch : ord(ch)-ord('A') })
training_data, test_data= data[:100,:],data[19990:,:]

knn = kNNClassifier()

start = time.time()
result = knn.classify(training_data,test_data)
print training_data
end = time.time()
print "It took " + str(end - start) + " seconds"