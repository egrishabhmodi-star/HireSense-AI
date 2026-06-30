import json
import numpy as np
from sentence_transformers import SentenceTransformer
from parser import read_candidates
from utils import candidate_text

print("Loading model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Loading candidates...")
candidates = read_candidates("../data/candidates.jsonl")

print("Total candidates:", len(candidates))

texts = []
candidate_ids = []

print("Preparing candidate texts...")

for candidate in candidates:
    texts.append(candidate_text(candidate))
    candidate_ids.append(candidate["candidate_id"])

print("Generating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=256,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Saving embeddings...")

np.save("../data/candidate_embeddings.npy", embeddings)

with open("../data/candidate_ids.json", "w") as f:
    json.dump(candidate_ids, f)

print("Done!")
print("Embeddings saved to ../data/candidate_embeddings.npy")
print("Candidate IDs saved to ../data/candidate_ids.json")