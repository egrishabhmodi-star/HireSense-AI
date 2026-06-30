from sentence_transformers import SentenceTransformer
from sentence_transformers import util

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding(text):

    return model.encode(
        text,
        convert_to_tensor=True
    )


def semantic_similarity(job_embedding, candidate_embedding):

    return util.cos_sim(
        job_embedding,
        candidate_embedding
    ).item()