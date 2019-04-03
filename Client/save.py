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
mysampleEvent=None
timestampEvent=None

def experiment2csv(experiment):
    pickle.dump( experiment, open( "save.p", "wb" ) )

def signal_handler(signal, frame):
    z.saveEEGCSV()
    z.saveMarkerCSV()
    sys.exit(0)

print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
print("Found EEG Stream")
print("looking for an Markers stream...")
stream2 = resolve_stream('type', 'Markers')
print("Found Markers Stream")

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
inletevent = StreamInlet(stream2[0])
signal.signal(signal.SIGINT, signal_handler)
while 1:

    # Pull EEG sample, convert to EEG object and append to EEG array
    mysample, timestamp = inlet.pull_sample()
    insertEEGSample=Sample(timestamp,mysample)
    # print(mysample)
    z.addEEGSample(insertEEGSample)

    # Pull Marker sample, convert to Marker object and append to Events array
    mysampleEvent, timestampEvent = inletevent.pull_sample(timeout=0.0)
    if mysampleEvent is not None:
        insertEventSample=Sample(timestampEvent,mysampleEvent)
        print(mysampleEvent)
        z.addEventSample(insertEventSample)

     

while 1:
    a=0