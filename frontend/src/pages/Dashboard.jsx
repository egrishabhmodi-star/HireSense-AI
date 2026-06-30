import { useState } from "react";
import Navbar from "../components/Navbar";
import ScoreCard from "../components/ScoreCard";
import UploadBox from "../components/UploadBox";
import CandidateTable from "../components/CandidateTable";
import { downloadCSV } from "../services/api";

function Dashboard() {
  const [candidates, setCandidates] = useState([]);

  return (
    <div className="min-h-screen bg-gray-100">

      <Navbar />

      <div className="max-w-7xl mx-auto p-8">

        <h2 className="text-3xl font-bold">
          Candidate Ranking Dashboard
        </h2>

        <p className="text-gray-600 mb-8">
          Upload a Job Description and instantly rank 100,000 candidates.
        </p>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

          <ScoreCard title="Candidates" value="100,000" color="text-blue-600" />
          <ScoreCard title="Top Matches" value="100" color="text-green-600" />
          <ScoreCard title="Runtime" value="9.1 s" color="text-orange-600" />
          <ScoreCard title="Model" value="MiniLM" color="text-purple-600" />

        </div>

        {/* Upload + Rank */}
        <UploadBox setCandidates={setCandidates} />

        {/* Download Button */}
        <div className="mt-6">
          <button
            onClick={downloadCSV}
            className="bg-green-600 text-white px-6 py-3 rounded-lg"
          >
            Download CSV
          </button>
        </div>

        {/* Table */}
        <CandidateTable candidates={candidates} />

        <p className="mt-6 text-xl font-bold">
          Total Ranked Candidates: {candidates.length}
        </p>

      </div>
    </div>
  );
}

export default Dashboard;