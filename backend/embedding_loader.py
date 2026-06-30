import numpy as np
import json

class EmbeddingStore:

    def __init__(self, emb_path, id_path):
        self.embeddings = np.load(emb_path)
        
        with open(id_path, "r") as f:
            self.ids = json.load(f)

        # map candidate_id → index
        self.id_to_index = {
            cid: i for i, cid in enumerate(self.ids)
        }

    def get(self, candidate_id):
        idx = self.id_to_index[candidate_id]
        return self.embeddings[idx]