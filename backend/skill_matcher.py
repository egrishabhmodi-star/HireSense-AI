from utils import get_skill_names

SKILL_WEIGHTS = {
    "python": 10,
    "machine learning": 10,
    "deep learning": 9,
    "llm": 9,
    "nlp": 8,
    "embeddings": 9,
    "retrieval": 9,
    "ranking": 9,
    "faiss": 8,
    "pinecone": 8,
    "weaviate": 8,
    "qdrant": 8,
    "milvus": 8,
    "sentence transformers": 8,
    "huggingface": 7,
    "tensorflow": 7,
    "pytorch": 7,
    "langchain": 6,
    "llamaindex": 6
}


def skill_score(candidate, required_skills):

    candidate_skills = get_skill_names(candidate)

    score = 0
    matched = []

    for skill in required_skills:

        if skill in candidate_skills:

            score += SKILL_WEIGHTS.get(skill, 5)
            matched.append(skill)

    return min(score, 20), matched