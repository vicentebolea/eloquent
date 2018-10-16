#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class EntryType:
  TWEET = 0
  LIKE = 1

  _VALUES_TO_NAMES = {
    0: "TWEET",
    1: "LIKE",
  }

  _NAMES_TO_VALUES = {
    "TWEET": 0,
    "LIKE": 1,
  }


class Entry:
  """
  Attributes:
   - type
   - message
   - liked_ref
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.STRING, 'message', None, None, ), # 2
    (3, TType.I32, 'liked_ref', None, None, ), # 3
  )

  def __init__(self, type=None, message=None, liked_ref=None,):
    self.type = type
    self.message = message
    self.liked_ref = liked_ref

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.liked_ref = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Entry')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 2)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    if self.liked_ref is not None:
      oprot.writeFieldBegin('liked_ref', TType.I32, 3)
      oprot.writeI32(self.liked_ref)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.type is None:
      raise TProtocol.TProtocolException(message='Required field type is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.message)
    value = (value * 31) ^ hash(self.liked_ref)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Block:
  """
  Attributes:
   - ref
   - pref
   - time
   - userid
   - signature
   - payload
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'ref', None, None, ), # 1
    (2, TType.I32, 'pref', None, None, ), # 2
    (3, TType.I32, 'time', None, None, ), # 3
    (4, TType.I32, 'userid', None, None, ), # 4
    (5, TType.I32, 'signature', None, None, ), # 5
    (6, TType.STRUCT, 'payload', (Entry, Entry.thrift_spec), None, ), # 6
  )

  def __init__(self, ref=None, pref=None, time=None, userid=None, signature=None, payload=None,):
    self.ref = ref
    self.pref = pref
    self.time = time
    self.userid = userid
    self.signature = signature
    self.payload = payload

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.ref = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.pref = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.time = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.userid = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.signature = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.payload = Entry()
          self.payload.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Block')
    if self.ref is not None:
      oprot.writeFieldBegin('ref', TType.I32, 1)
      oprot.writeI32(self.ref)
      oprot.writeFieldEnd()
    if self.pref is not None:
      oprot.writeFieldBegin('pref', TType.I32, 2)
      oprot.writeI32(self.pref)
      oprot.writeFieldEnd()
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I32, 3)
      oprot.writeI32(self.time)
      oprot.writeFieldEnd()
    if self.userid is not None:
      oprot.writeFieldBegin('userid', TType.I32, 4)
      oprot.writeI32(self.userid)
      oprot.writeFieldEnd()
    if self.signature is not None:
      oprot.writeFieldBegin('signature', TType.I32, 5)
      oprot.writeI32(self.signature)
      oprot.writeFieldEnd()
    if self.payload is not None:
      oprot.writeFieldBegin('payload', TType.STRUCT, 6)
      self.payload.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.ref is None:
      raise TProtocol.TProtocolException(message='Required field ref is unset!')
    if self.pref is None:
      raise TProtocol.TProtocolException(message='Required field pref is unset!')
    if self.time is None:
      raise TProtocol.TProtocolException(message='Required field time is unset!')
    if self.userid is None:
      raise TProtocol.TProtocolException(message='Required field userid is unset!')
    if self.signature is None:
      raise TProtocol.TProtocolException(message='Required field signature is unset!')
    if self.payload is None:
      raise TProtocol.TProtocolException(message='Required field payload is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ref)
    value = (value * 31) ^ hash(self.pref)
    value = (value * 31) ^ hash(self.time)
    value = (value * 31) ^ hash(self.userid)
    value = (value * 31) ^ hash(self.signature)
    value = (value * 31) ^ hash(self.payload)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BlockChain:
  """
  Attributes:
   - world
  """

  thrift_spec = (
    None, # 0
    (1, TType.SET, 'world', (TType.STRUCT,(Block, Block.thrift_spec)), None, ), # 1
  )

  def __init__(self, world=None,):
    self.world = world

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.SET:
          self.world = set()
          (_etype3, _size0) = iprot.readSetBegin()
          for _i4 in xrange(_size0):
            _elem5 = Block()
            _elem5.read(iprot)
            self.world.add(_elem5)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BlockChain')
    if self.world is not None:
      oprot.writeFieldBegin('world', TType.SET, 1)
      oprot.writeSetBegin(TType.STRUCT, len(self.world))
      for iter6 in self.world:
        iter6.write(oprot)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.world is None:
      raise TProtocol.TProtocolException(message='Required field world is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.world)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
