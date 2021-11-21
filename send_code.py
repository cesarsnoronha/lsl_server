import sys
import grpc
from lsl_pb2_grpc import LSLMessageStub
from lsl_pb2 import LSLRequest

CODE = int(sys.argv[1])
print(CODE)

channel = grpc.insecure_channel("localhost:50051")
client = LSLMessageStub(channel)
request = LSLRequest(state=CODE)
client.SendMessage(request)

# from pylsl import StreamInfo, StreamOutlet

# # sets variables for object info
# info = StreamInfo(name='Trigger', type='Markers', channel_count=1, channel_format='int32', source_id='Example')

# # initialize stream.
# outlet = StreamOutlet(info)
# outlet.push_sample(x=[CODE])
