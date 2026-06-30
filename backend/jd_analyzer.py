IMPORTANT_SKILLS = [
    "python",
    "embeddings",
    "retrieval",
    "ranking",
    "vector database",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "opensearch",
    "elasticsearch",
    "llm",
    "fine tuning",
    "lora",
    "qlora",
    "peft",
    "machine learning",
    "sentence transformers",
    "huggingface"
]


def extract_requirements(job_text):
    """
    Extract important skills mentioned in the Job Description.
    """
    job_text = job_text.lower()

    found = []

    for skill in IMPORTANT_SKILLS:
        if skill in job_text:
            found.append(skill)

    return found