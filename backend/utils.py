def get_skill_names(candidate):
    skills = []

    for skill in candidate.get("skills", []):
        skills.append(skill["name"].lower())

    return skills


def get_total_experience(candidate):
    return candidate["profile"]["years_of_experience"]


def get_current_title(candidate):
    return candidate["profile"]["current_title"].lower()


def candidate_text(candidate):

    text = ""

    profile = candidate["profile"]

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for skill in candidate.get("skills", []):
        text += skill.get("name", "") + " "

    for job in candidate.get("career_history", []):
        text += job.get("title", "") + " "
        text += job.get("description", "") + " "

    return text


def career_text(candidate):

    text = ""

    for job in candidate.get("career_history", []):
        text += job.get("title", "") + " "
        text += job.get("description", "") + " "
        text += job.get("industry", "") + " "

    return text.lower()


AI_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "data scientist",
    "nlp engineer",
    "search engineer",
    "recommendation engineer",
    "deep learning engineer",
    "senior machine learning engineer"
]


def is_ai_role(candidate):

    title = candidate["profile"]["current_title"].lower()

    for role in AI_TITLES:
        if role in title:
            return True

    return False


PRODUCT_KEYWORDS = [
    "product",
    "search",
    "recommendation",
    "ranking",
    "retrieval",
    "machine learning",
    "artificial intelligence",
    "llm"
]


def product_experience(candidate):

    text = career_text(candidate)

    score = 0

    for word in PRODUCT_KEYWORDS:
        if word in text:
            score += 1

    return score


GOOD_ROLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "data scientist",
    "nlp engineer",
    "search engineer",
    "recommendation engineer",
    "deep learning engineer",
    "senior machine learning engineer"
]


BAD_ROLES = [
    "marketing manager",
    "sales executive",
    "accountant",
    "graphic designer",
    "customer support",
    "hr manager",
    "civil engineer",
    "mechanical engineer",
    "content writer"
]


def role_penalty(candidate):

    title = candidate["profile"]["current_title"].lower()

    for role in GOOD_ROLES:
        if role in title:
            return 10

    for role in BAD_ROLES:
        if role in title:
            return -15

    return 0