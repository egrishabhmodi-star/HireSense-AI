import csv


def export_submission(
    ranked_candidates,
    filename="../output/submission.csv"
):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ])

        for rank, candidate in enumerate(
            ranked_candidates[:100],
            start=1
        ):

            writer.writerow([
                candidate["candidate_id"],
                rank,
                round(candidate["score"], 4),
                candidate["reasoning"]
            ])

    print("Submission saved.")