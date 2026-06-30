function CandidateTable({ candidates }) {

    if (!candidates || candidates.length === 0) {
        return <p className="mt-6 text-gray-500">No candidates ranked yet.</p>;
    }

    return (
        <div className="mt-8 overflow-x-auto">
            <table className="min-w-full bg-white shadow rounded-lg">

                <thead>
                    <tr className="bg-gray-100 text-left">
                        <th className="p-3">Rank</th>
                        <th className="p-3">Candidate ID</th>
                        <th className="p-3">Score</th>
                        <th className="p-3">Reason</th>
                    </tr>
                </thead>

                <tbody>
                    {candidates.map((c, index) => (
                        <tr key={c.candidate_id} className="border-t">
                            <td className="p-3">{index + 1}</td>
                            <td className="p-3">{c.candidate_id}</td>
                            <td className="p-3">{c.score}</td>
                            <td className="p-3 text-sm text-gray-600">
                                {c.reasoning}
                            </td>
                        </tr>
                    ))}
                </tbody>

            </table>
        </div>
    );
}

export default CandidateTable;