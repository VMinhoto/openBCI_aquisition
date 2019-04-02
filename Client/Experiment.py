import datetime
import numpy as np
import csv
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

    def saveCSV(self):
        with open('Experiment.csv', mode='w') as experiment_file:
            experiment_writer = csv.writer(experiment_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            experiment_writer.writerow(['Timestamp',"0","1","2","3","4","5","6","7"])
            for element in self.eeg:
                experiment_writer.writerow(np.append(element.timestamp,element.value))

class Sample:
    def __init__(self,timestamp,value):
        self.timestamp=timestamp
        self.value=value