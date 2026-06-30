# 🚀 HireSense AI - Explainable Candidate Ranking Engine

> An AI-powered recruitment intelligence system that ranks candidates by understanding job requirements, skills, experience, and behavioral signals instead of relying on simple keyword matching.

## 📌 Problem Statement

Traditional Applicant Tracking Systems (ATS) often rank resumes based on keyword matching, causing highly qualified candidates to be overlooked.

HireSense AI solves this by using AI-driven semantic analysis and hybrid scoring to identify candidates who genuinely fit a job description.

---

## 🎯 Features

- 📄 Understands Job Descriptions
- 👨‍💼 Intelligent Candidate Ranking
- 🧠 Semantic Skill Matching
- 📊 Hybrid Scoring Algorithm
- 📈 Behavioral Signal Analysis
- 💡 Explainable AI Recommendations
- 📋 Candidate Summary
- ❓ AI-Generated Interview Questions
- 📂 Export Ranked Candidate List

---

## 🏗️ Project Architecture
Job Description
│
▼
Requirement Extraction
│
▼
Candidate Dataset
│
▼
Feature Extraction
│
▼
Hybrid Scoring Engine
│
├── Skill Match
├── Experience Match
├── Semantic Similarity
├── Behavioral Signals
└── Consistency Checks
│
▼
Candidate Ranking
│
▼
Top Candidates + Explanation


---

## 🛠️ Tech Stack

### Frontend
- React.js
- Vite
- CSS

### Backend
- FastAPI
- Python

### AI & Data Processing
- Pandas
- Sentence Transformers
- Scikit-learn
- JSON
- python-docx

### Version Control
- Git
- GitHub

---

## 📁 Project Structure
HireSense-AI/
│
├── backend/
│ ├── main.py
│ ├── parser.py
│ ├── scorer.py
│ ├── ranker.py
│ ├── utils.py
│ ├── config.py
│ └── requirements.txt
│
├── frontend/
│
├── data/
│
├── output/
│
├── docs/
│
├── screenshots/
│
└── README.md


---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/HireSense-AI.git

cd HireSense-AI
Backend Setup
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
Backend will run at:

http://127.0.0.1:8000
Frontend Setup
cd frontend

npm install

npm run dev
Frontend will run at:

http://localhost:5173
🚀 Workflow
Load Job Description

Read Candidate Dataset

Extract Skills & Requirements

Calculate Candidate Scores

Rank Candidates

Generate Explainable Results

Export Ranked Candidate List

📊 Scoring Factors
Our hybrid ranking engine evaluates candidates using multiple dimensions:

Technical Skills

Work Experience

Semantic Job Match

Career Progression

Behavioral Signals

Profile Completeness

Profile Consistency

Instead of keyword matching, HireSense AI performs holistic candidate evaluation similar to how an experienced recruiter would.

💡 Why HireSense AI?
Unlike traditional ATS systems, HireSense AI:

Understands job requirements semantically

Produces explainable rankings

Reduces keyword bias

Considers multiple candidate signals

Improves recruiter decision-making

📈 Future Enhancements
Chrome Extension

Recruiter Dashboard

PDF Resume Parsing

Candidate Comparison Dashboard

Learning-based Ranking Optimization

Multi-language Resume Support

👥 Team
Rishabh Modi

Anmol Singh

Team Member 3




⭐ If you found this project interesting, consider giving it a star!
