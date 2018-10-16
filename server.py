import glob
import sys
sys.path.append('gen-py')

from eloquent import Eloquent
from eloquent.ttypes import EntryType, BlockChain, Block, Entry

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class EloquentHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def submit_block(self, msg):
        #msg.entry
        #if msg.entry == Operation.ADD:
        #    val = work.num1 + work.num2
        #elif work.op == Operation.SUBTRACT:
        #    val = work.num1 - work.num2
        #elif work.op == Operation.MULTIPLY:
        #    val = work.num1 * work.num2
        #elif work.op == Operation.DIVIDE:
        pass

if __name__ == '__main__':
    handler = EloquentHandler()
    processor = Eloquent.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    server.serve()
