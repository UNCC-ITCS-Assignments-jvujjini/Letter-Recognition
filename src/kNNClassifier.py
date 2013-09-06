import math

class kNNClassifier():
    
    def classify(self,training_set,test_set):  
        
        result = []  
        num = 0    
        
        for case in test_set:
            
            min_diff = float("inf")
            
            for example in training_set:
                
                diff = self.diff(example,case)
                
                if diff < min_diff:
                    min_diff = diff
                    min_diff_index = example[0]
                
            test_result = min_diff_index
            num = num + 1
            print str(num) +":"+ str(test_result)+":"+str(diff)
            result.append(test_result)
            
        return result
            
    def diff(self,train,test):
        
        sigma = 0
        attributes_length = len(test)
        
        for k in xrange(1,attributes_length):
            sigma += (test[k]-train[k])**2
        
        ans = (1/attributes_length-1) * float(math.sqrt(sigma))
        
        return ans