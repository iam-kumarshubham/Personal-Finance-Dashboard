import { useNetWorth, useDeleteNetWorthEntry } from "../hooks/useNetWorth";

const NetWorthList = () => {
  const { data, isLoading, error } = useNetWorth() as { data: { id: string; assets: number; liabilities: number; }[]; isLoading: boolean; error: any };
  const deleteEntry = useDeleteNetWorthEntry();

  if (isLoading) return <p>Loading net worth data...</p>;
  if (error) return <p>Error loading data.</p>;

  return (
    <div className="p-4">
      <h2 className="text-lg font-bold mb-2">Net Worth History</h2>
      <ul className="space-y-2">
        {data.map((entry: any) => (
          <li key={entry.id} className="flex justify-between items-center p-2 border rounded bg-gray-100">
            <span>
              Assets: ${entry.assets} | Liabilities: ${entry.liabilities} | Net Worth: ${entry.assets - entry.liabilities}
            </span>
            <button onClick={() => deleteEntry.mutate(entry.id)} className="text-red-500">
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NetWorthList;
