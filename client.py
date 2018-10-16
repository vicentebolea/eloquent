import sys
import glob
sys.path.append('gen-py')

from eloquent import Eloquent
from eloquent.ttypes import EntryType, BlockChain, Block, Entry

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Eloquent.Client(protocol)
    transport.open()

    client.ping()
    print('ping()')

    #sum_ = client.add(1, 1)
    #print('1+1=%d' % sum_)

    #work = Work()

    #work.op = Operation.DIVIDE
    #work.num1 = 1
    #work.num2 = 0

    #try:
    #    quotient = client.calculate(1, work)
    #    print('Whoa? You know how to divide by zero?')
    #    print('FYI the answer is %d' % quotient)
    #except InvalidOperation as e:
    #    print('InvalidOperation: %r' % e)

    #work.op = Operation.SUBTRACT
    #work.num1 = 15
    #work.num2 = 10

    #diff = client.calculate(1, work)
    #print('15-10=%d' % diff)

    #log = client.getStruct(1)
    #print('Check log: %s' % log.value)

    # Close!
    transport.close()

if __name__ == '__main__':
    main()
