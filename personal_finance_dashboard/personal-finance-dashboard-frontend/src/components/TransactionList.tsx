import { useTransactions, useDeleteTransaction } from "../hooks/useTransactions";

const TransactionList = () => {
  const { data, isLoading, error } = useTransactions();
  const deleteTransaction = useDeleteTransaction();

  if (isLoading) return <p>Loading transactions...</p>;
  if (error) return <p>Error loading transactions.</p>;

  return (
    <div className="p-4">
      <h2 className="text-lg font-bold mb-2">Transactions</h2>
      <ul className="space-y-2">
        {data && data.map((transaction: any) => (
          <li key={transaction.id} className="flex justify-between items-center p-2 border rounded bg-gray-100">
            <span>{transaction.category} - ${transaction.amount}</span>
            <button onClick={() => deleteTransaction.mutate(transaction.id)} className="text-red-500">
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionList;
