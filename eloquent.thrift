namespace py eloquent

enum EntryType {
  TWEET,
  LIKE
}

struct Entry {
   1: required EntryType type,
   2: optional string message,
   3: optional i32 liked_ref,
}

struct Block {
  1: required i32 ref,
  2: required i32 pref,
  3: required i32 time,
  4: required i32 userid,
  5: required i32 signature,
  6: required Entry payload
}

struct BlockChain {
  1: required set<Block> world
}

service Eloquent {
   void ping(),
   bool submit_block(1:Block msg),
   string request_blockchain(1:i64 last_ref),
   void whisper(1:set<string> nodes)
} 
