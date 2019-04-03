from pylsl import StreamInlet, resolve_stream

# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'Markers')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])
info = inlet.info()
#print("The stream's XML meta-data is: ")
#print(info.as_xml())

while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    print(timestamp, sample)