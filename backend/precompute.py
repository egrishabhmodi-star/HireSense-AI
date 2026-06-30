def preprocess(candidates):

    for c in candidates:

        profile = c["profile"]
        signals = c["redrob_signals"]

        # numeric features ONLY
        c["exp"] = profile["years_of_experience"]
        c["ai_role"] = profile["current_title"].lower()

        c["behaviour_score"] = (
            signals["recruiter_response_rate"] * 5 +
            signals["interview_completion_rate"] * 5 +
            min(signals["saved_by_recruiters_30d"], 5)
        )

        c["availability_score"] = (
            (5 if signals["open_to_work_flag"] else 0) +
            (5 if signals["notice_period_days"] <= 30 else 0)
        )

        c["profile_score"] = (
            (signals["profile_completeness_score"] / 100) * 5 +
            (2 if signals["verified_email"] else 0) +
            (2 if signals["verified_phone"] else 0) +
            (1 if signals["linkedin_connected"] else 0)
        )

    return candidates