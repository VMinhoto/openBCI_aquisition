from Experiment import Experiment,Sample
import time
import datetime
from random import random as rand
z=Experiment("Vitor",1)
x=500
stopvar=500
while x:
    # make a new random 8-channel sample; this is converted into a
    # pylsl.vectorf (the data type that is expected by push_sample)
    mysample = [rand(), rand(), rand(), rand(), rand(), rand(), rand(), rand()]
    insertEEGSample=Sample(int(round(time.time() * 1000)),mysample)
    if x==stopvar:
        insertEventSample=Sample(int(round(time.time() * 1000)),1)
        z.addEventSample(insertEventSample)
        stopvar-=50

    # now send it and wait for a bit
    z.addEEGSample(insertEEGSample)
    time.sleep(0.01)
    x-=1

while 1:
    a=0