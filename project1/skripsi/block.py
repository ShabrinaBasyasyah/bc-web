import hashlib
import json

class block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        data_encoded = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(str(self.timestamp).encode() + data_encoded + str(self.previous_hash).encode()).hexdigest()
    
    def to_dict(self):
        return{
            "timestamp": self.timestamp,
            "data": self.data.to_dict(),
            "previous_hash": self.previous_hash,
            "hash": self.hash
        }
    
    def has_same_ids(self, other_block):
        return (
            self.data.id_penawaran == other_block.data.id_penawaran and
            self.data.id_periode_penawaran == other_block.data.id_periode_penawaran and
            self.data.id_permintaan == other_block.data.id_permintaan and
            self.data.id_periode_permintaan == other_block.data.id_periode_permintaan
        )

@classmethod
def from_dict(cls, block_dict):
    return cls(block_dict["timestamp"], block_dict["data"], block_dict["previous_hash"])