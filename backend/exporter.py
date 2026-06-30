import pandas as pd

def export_csv(ranked_candidates, filename="../output/submission.csv"):

    rows = []

    for i, candidate in enumerate(ranked_candidates[:100], start=1):

        rows.append({
            "candidate_id": candidate["candidate_id"],
            "rank": i,
            "score": round(candidate["score"], 4),
            "reasoning": candidate["reasoning"]
        })

    df = pd.DataFrame(rows)

    df.to_csv(filename, index=False)

    print("Submission file created!")