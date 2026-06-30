from docx import Document
import json


# -----------------------------
# Read Job Description (.docx)
# -----------------------------
def read_job_description(file_path):
    """
    Reads the job description from a DOCX file.
    Returns the complete text.
    """

    doc = Document(file_path)

    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)

    return "\n".join(text)


# -----------------------------
# Read Candidates (.jsonl)
# -----------------------------
def read_candidates(file_path):
    """
    Reads all candidate profiles from a JSONL file.
    Returns a list of candidate dictionaries.
    """

    candidates = []

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:
            candidates.append(json.loads(line))

    return candidates
    from config import MANDATORY_SKILLS, PREFERRED_SKILLS

def analyze_job_description(job_text):
    """
    Extracts important requirements from the JD.
    """

    job_text = job_text.lower()

    mandatory = []
    preferred = []

    for skill in MANDATORY_SKILLS:
        if skill in job_text:
            mandatory.append(skill)

    for skill in PREFERRED_SKILLS:
        if skill in job_text:
            preferred.append(skill)

    return {
        "mandatory_skills": mandatory,
        "preferred_skills": preferred,

        "max_notice_period": 30
    }