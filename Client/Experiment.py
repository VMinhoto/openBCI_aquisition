import datetime
import numpy as np
class Experiment:
    def __init__(self,name,Ttype):
        self.subjectName=name
        self.date=datetime.datetime.now()
        self.trialType=Ttype
        self.eeg=np.empty((0))
        self.events=np.empty((0))
    
    def addEEGSample(self,sample):
        self.eeg=np.append(self.eeg,sample)

    def addEventSample(self,sample):
        self.events=np.append(self.events,sample)

class Sample:
    def __init__(self,timestamp,value):
        self.timestamp=timestamp
        self.value=value