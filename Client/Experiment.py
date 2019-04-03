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

    def saveEEGCSV(self):
        filename=str(self.date.year)+"-"+str(self.date.month)+"-"+str(self.date.day)+"-"+str(self.date.hour)+"-"+str(self.date.minute)+"-"+str(self.date.second)+"BRAINLab-"+self.subjectName
        with open(filename+"-EEG.csv", mode='w') as eeg_file:
            eeg_writer = csv.writer(eeg_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            eeg_writer.writerow(['Timestamp',"0","1","2","3","4","5","6","7"])
            for element in self.eeg:
                eeg_writer.writerow(np.append(element.timestamp,element.value))
    def saveMarkerCSV(self):
        filename=str(self.date.year)+"-"+str(self.date.month)+"-"+str(self.date.day)+"-"+str(self.date.hour)+"-"+str(self.date.minute)+"-"+str(self.date.second)+"BRAINLab-"+self.subjectName
        with open(filename+"-Events.csv", mode='w') as markers_file:
            markers_writer = csv.writer(markers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            markers_writer.writerow(['Timestamp','Marker'])
            for element in self.events:
                markers_writer.writerow(np.append(element.timestamp,element.value))


class Sample:
    def __init__(self,timestamp,value):
        self.timestamp=timestamp
        self.value=value