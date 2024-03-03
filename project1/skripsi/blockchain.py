from datetime import datetime
from penawaran import penawaran
from permintaan import permintaan
from pembeli import pembeli
from penjual import penjual
from transaksi_jual import transaksi_jual
from transaksi_beli import transaksi_beli
from block import block

class blockchain:
    def __init__(self):
        self.blocks = []
        self.genesis_block = block(0, {"transactions": []}, "0")
        self.blocks.append(self.genesis_block)
        
    def add_block(self, transactions):
        data = {"transactions": []}
        for transaction in transactions:
            if isinstance(transaction, (permintaan, penawaran, transaksi_beli, transaksi_jual)):
                data["transactions"].append(transaction.to_dict())
            else:
                raise ValueError("Data yang diberikan tidak valid")
            
        new_block = block(datetime.now().timestamp(), data, self.blocks[-1].hash)
        self.blocks.append(new_block)
    
    def get_latest_block(self):
        return self.blocks[-1]
    
    def calculate_total_emisions(self):
        total_emisions = 0
        for block in self.blocks:
            for transaction in block.data["transactions"]:
                if "jumlah_karbon_masuk" in transaction:
                    total_emissions += transaction["jumlah_karbon_masuk"]
                elif "jumlah_karbon_keluar" in transaction:
                    total_emisions -= transaction["jumlah_karbon_keluar"]
            return total_emisions
    
    def to_dict(self):
        return {
            "blocks": [block.to_dict() for block in self.blocks], 
            "total_emisions": self.calculate_total_emisions()
        }
    
    def __repr__(self):
        return f"Blockchain(blocks=[\n" + "\n".join(
            [
                f"    Block(timestamp={block.timestamp}, data={block.data}, previous_hash={block.previous_hash})"
                for block in self.blocks
            ]
        ) + f"\n], total_emissions={self.calculate_total_emissions()}"