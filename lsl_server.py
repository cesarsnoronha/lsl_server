from concurrent import futures

import random
import grpc
import sys
from pylsl import StreamInfo, StreamOutlet

from lsl_pb2 import (State, LSLRequest, LSLResponse)
import lsl_pb2_grpc

# sets variables for object info
info = StreamInfo(name='Trigger', type='Markers', channel_count=1, channel_format='int32', source_id='Example')

# initialize stream.
outlet = StreamOutlet(info)

class LSLService(lsl_pb2_grpc.LSLMessageServicer):
    def SendMessage(self, request, context):
        LSL_code = request.state + 1
        print('Sending code: {}'.format(LSL_code))
        outlet.push_sample(x=[LSL_code])
        return LSLResponse(id=request.state, description="TEST")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lsl_pb2_grpc.add_LSLMessageServicer_to_server(
        LSLService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()