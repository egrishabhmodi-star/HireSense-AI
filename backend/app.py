from flask import Flask, jsonify, send_file
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

# load job ONCE (faster)
job = read_job_description("../data/job_description.docx")


@app.route("/rank", methods=["GET"])
def rank():
    try:
        ranked = rank_candidates(job, candidates, store)
        return jsonify(ranked[:100])
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download")
def download():
    return send_file("../output/submission.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)