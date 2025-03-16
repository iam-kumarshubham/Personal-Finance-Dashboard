import { useState } from "react";
import TransactionList from "../components/TransactionList";
import TransactionForm from "../components/TransactionForm";

const Transactions = () => {
  const [showForm, setShowForm] = useState(false);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Transactions</h1>
      <button onClick={() => setShowForm(true)} className="mb-4 bg-green-500 text-white p-2 rounded">
        Add Transaction
      </button>

      {showForm && <TransactionForm onClose={() => setShowForm(false)} />}
      <TransactionList />
    </div>
  );
};

export default Transactions;
