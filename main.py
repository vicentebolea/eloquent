#!/bin/env python
import json
import time
import os
import sys

# Looks like
# ref      | parent ref | userid    | msg                | Sign | 
# ------------------------------------------------
# #sdsadas | #0         | userid=0  | msg="hello world"
# #S123sad | #sdsadas   | userid=1  | msg="hi there"
# #sdasdad | #S123sad   | userid=2  | msg="trool"

class Eloquent:
    def __init__(self):
        pass

    def append_block(self, bundle):
        parent_ref = 00000000
        row = ""
        history = [ ]
        if os.path.isfile("data") and os.stat("data").st_size > 0:
            f = open("data", "r+")
            history = json.load(f)
            last = history[-1]
            parent_ref = last['ref']
            f.close()

        f = open("data", "w+")

        ref = hash(str(bundle))

        schema = { "ref": ref, "pref": parent_ref, 'content': bundle}
        history.append(schema)
        row = json.dumps(history, separators= ("\n,", ':'))

        f.write(row)
        f.close()

    def read_msg(self, userid = -1):
        if os.path.isfile("data") and os.stat("data").st_size > 0:
            f = open("data", "r+")
            history = json.load(f)
            for item in history:
                if item['content']['userid'] == userid or userid == -1:
                    kv = item['content']
                    print str("user " + str(kv['userid']) +" said on "  + kv['time'] + " >>> "  + kv['msg'] )
            f.close()


    def write_msg(self, userid, msg):
        bundle = {"userid" : userid, "msg" : msg, "time": time.ctime()}
        self.append_block(bundle)

def parse_args(args, eloquent):

    if len(args) < 3:
        print "Call like: eloquent ACTION args"
        sys.exit(-1)

    action = args[1]
    userid = int(args[2])

    msg    =""
    if len(args) > 3:
        msg= args[3]

    if (action == "write"):
        eloquent.write_msg(userid, msg)


    if (action == "read"):
        eloquent.read_msg(userid)


e = Eloquent()
parse_args(sys.argv, e)
