from semantic_match import get_embedding
from scorer import calculate_score


def rank_candidates(job_text, candidates, store):

    job_embedding = get_embedding(job_text)

    ranked = []

    for candidate in candidates:

        candidate_embedding = store.get(candidate["candidate_id"])

        score, reasons = calculate_score(
            job_embedding,
            candidate_embedding,
            candidate
        )

        ranked.append({
            "candidate_id": candidate["candidate_id"],
            "score": score,
            "reasoning": "; ".join(reasons)
        })

    ranked.sort(
        key=lambda x: (-x["score"], x["candidate_id"])
    )

    return ranked[:100]