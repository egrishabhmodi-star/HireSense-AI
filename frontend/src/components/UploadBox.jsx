import { useState } from "react";
import API from "../services/api";

function UploadBox({ setCandidates }) {

    const [loading, setLoading] = useState(false);

    async function rankCandidates() {

        setLoading(true);

        try {

            const res = await API.get("/rank");

            setCandidates(res.data);

        } catch (err) {

            console.log(err.response?.data || err.message);
            alert("Backend Error");

        }

        setLoading(false);
    }

    return (
        <div className="bg-white p-6 rounded-xl shadow">

            <button
                onClick={rankCandidates}
                className="bg-blue-600 text-white px-6 py-3 rounded-lg"
            >
                {loading ? "Ranking..." : "Rank Candidates"}
            </button>

        </div>
    );
}

export default UploadBox;