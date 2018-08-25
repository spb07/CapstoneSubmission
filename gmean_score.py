import pandas as pd

class Gscore():
    def __init__(self, y_act, y_predi):
        self.y_actual = y_act
        self.y_pred = y_predi
        self.TP = 0 # True positive
        self.FP = 0 # False positive
        self.TN = 0 # True negative
        self.FN = 0 # False negative
        self.pred()
        
    def convert_df_to_ndarray(self, X):
        print(type(X))
        if type(X) == 'pandas.core.frame.DataFrame' or type(X) == 'pandas.core.series.Series':
            print("Successfully converted")
            return X.values
        print("No conversion done") 
        return X
        
    def pred(self):
        for i in range(len(self.y_pred)): 
            if self.y_actual[i] == self.y_pred[i] == 1: # Correct identification of Bad RiskPerformance
               self.TN += 1
            if self.y_pred[i] == 1 and self.y_actual[i] != self.y_pred[i]: # Incorrect classified Good RiskPerformance as Bad
               self.FN += 1
            if self.y_actual[i] == self.y_pred[i] == 0: # Correct identification of Good RiskPerformance
               self.TP += 1
            if self.y_pred[i] == 0 and self.y_actual[i] != self.y_pred[i]: # Incorrect classified Good RiskPerformance as Bad
               self.FP += 1
        '''
        #print('Manual metrics: ', TN, FN,TP,FP)
        sensi = TP/(TP+FN)
        speci = TN/(TN+FP)

        return sensi*speci
        '''
        return (self.TP,self.FP, self.TN, self.FN)

    def sensi(self):
        return self.TP/(self.TP+self.FN)

    def speci(self):
        return self.TN/(self.TN+self.FP)

    def g_mean(self):
        return (self.sensi()* self.speci())**0.5


        




