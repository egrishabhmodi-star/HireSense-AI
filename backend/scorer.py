from semantic_match import semantic_similarity
from skill_matcher import skill_score
from jd_analyzer import extract_requirements


def calculate_score(job_embedding, candidate_embedding, candidate):

    s1 = semantic_similarity(job_embedding, candidate_embedding) * 35

    profile = candidate["redrob_signals"]

    profile_score = profile["profile_completeness_score"] / 20

    availability = 5 if profile["open_to_work_flag"] else 0

    saved = min(profile["saved_by_recruiters_30d"], 5)

    required = [
        "python",
        "embeddings",
        "faiss",
        "pinecone"
    ]

    skill_marks, matched = skill_score(candidate, required)

    total = (
        s1
        + skill_marks
        + profile_score
        + availability
        + saved
    )

    reasons = [
        f"Semantic Match: {round(s1,1)}",
        f"AI Skills: {', '.join(matched) if matched else 'None'}",
        f"Profile: {round(profile_score,1)}",
        f"Open to Work: {availability}",
        f"Saved Signals: {saved}"
    ]

    return round(total, 2), reasons