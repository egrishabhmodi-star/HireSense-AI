from parser import read_job_description, read_candidates
from embedding_loader import EmbeddingStore
from ranker import rank_candidates
from export_csv import export_submission
import time

start = time.time()

print("Loading Job Description...")
job = read_job_description("../data/job_description.docx")

print("Loading Candidates...")
candidates = read_candidates("../data/candidates.jsonl")

print("Creating Embedding Store...")
store = EmbeddingStore(
    "../data/candidate_embeddings.npy",
    "../data/candidate_ids.json"
)

print("Ranking Candidates...")
ranked = rank_candidates(job, candidates, store)

print("\nTop 100 Candidates\n")

for i, c in enumerate(ranked[:100], 1):
    print("=" * 60)
    print(f"Rank #{i}")
    print("Candidate:", c["candidate_id"])
    print("Score:", round(c["score"], 2))
    print("Reason:")
    print(c["reasoning"])

print("\nExporting CSV...")
export_submission(ranked)

print("\nDone in:", round(time.time() - start, 2), "seconds")