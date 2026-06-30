from flask import Flask, jsonify
from flask_cors import CORS

from parser import read_job_description, read_candidates
from embedding_loader import EmbeddingStore
from ranker import rank_candidates

app = Flask(__name__)
CORS(app)

print("Loading candidates...")
candidates = read_candidates("../data/candidates.jsonl")

print("Loading embedding store...")
store = EmbeddingStore(
    "../data/candidate_embeddings.npy",
    "../data/candidate_ids.json"
)


@app.route("/rank", methods=["GET"])
def rank():

    job = read_job_description("../data/job_description.docx")

    ranked = rank_candidates(job, candidates, store)

    return jsonify(ranked)


if __name__ == "__main__":
    app.run(debug=True)