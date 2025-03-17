import { useEffect, useState } from "react";
import { fetchTransactions, addTransaction, deleteTransaction } from "../api/transactions";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import Button from "../components/Button";
import Input from "../components/Input";

interface Transaction {
  id: number;
  type: string;
  category: string;
  amount: number;
}

const Transactions = () => {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [newTransaction, setNewTransaction] = useState({ type: "income", category: "", amount: 0 });

  useEffect(() => {
    const getTransactions = async () => {
      try {
        const data = await fetchTransactions();
        setTransactions(data);
      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
    };

    getTransactions();
  }, []);

  const handleAddTransaction = async () => {
    try {
      const addedTransaction = await addTransaction(newTransaction);
      if (addedTransaction) {
        setTransactions([...transactions, addedTransaction]);
      }
      setNewTransaction({ type: "income", category: "", amount: 0 });
    } catch (error) {
      console.error("Error adding transaction:", error);
    }
  };

  const handleDeleteTransaction = async (id: number) => {
    try {
      await deleteTransaction(id);
      setTransactions(transactions.filter((tx) => tx.id !== id));
    } catch (error) {
      console.error("Error deleting transaction:", error);
    }
  };

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h2 className="text-2xl font-semibold my-4">Transactions</h2>

        {/* Add Transaction Form */}
        <div className="bg-white p-4 rounded-lg shadow-md mb-4">
          <h3 className="text-lg font-semibold mb-2">Add Transaction</h3>
          <Input
            label="Category"
            value={newTransaction.category}
            onChange={(e) => setNewTransaction({ ...newTransaction, category: e.target.value })}
          />
          <Input
            label="Amount"
            type="number"
            value={newTransaction.amount.toString()}
            onChange={(e) => setNewTransaction({ ...newTransaction, amount: Number(e.target.value) })}
          />
          <Button text="Add Transaction" onClick={handleAddTransaction} />
        </div>

        {/* Transactions List */}
        <div className="bg-white p-4 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-2">Recent Transactions</h3>
          <ul>
            {transactions.map((tx) => (
              <li key={tx.id} className="border-b py-2 flex justify-between">
                <span>{tx.category}</span>
                <span className={tx.type === "income" ? "text-green-500" : "text-red-500"}>
                  ${tx.amount}
                </span>
                <Button text="Delete" onClick={() => handleDeleteTransaction(tx.id)} />
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Transactions;
