from Experiment import Experiment,Sample
import time
import datetime
from random import random as rand
from pylsl import StreamInlet, resolve_stream
import signal
import sys
import pickle


z=Experiment("Vitor",1)
x=500
stopvar=500

def experiment2csv(experiment):
    pickle.dump( experiment, open( "save.p", "wb" ) )

def signal_handler(signal, frame):
    a=z
    a.saveCSV()
    sys.exit(0)

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

signal.signal(signal.SIGINT, signal_handler)
while inlet.info():
    # make a new random 8-channel sample; this is converted into a
    # pylsl.vectorf (the data type that is expected by push_sample)
    mysample, timestamp = inlet.pull_sample()
    #mysample = [rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()]
    insertEEGSample=Sample(timestamp,mysample)
    """ if x==stopvar:
        insertEventSample=Sample(int(round(time.time() * 1000)),1)
        z.addEventSample(insertEventSample)
        stopvar-=50 """

    # now send it and wait for a bit
    z.addEEGSample(insertEEGSample)
    time.sleep(0.01)
    print(x)
    

while 1:
    a=0