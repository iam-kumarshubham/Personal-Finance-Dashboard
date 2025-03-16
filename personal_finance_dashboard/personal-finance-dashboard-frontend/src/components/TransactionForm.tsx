import { useState } from "react";
import { useAddTransaction, useEditTransaction } from "../hooks/useTransactions";

const TransactionForm = ({ existingTransaction, onClose }: { existingTransaction?: any; onClose: () => void }) => {
  const [formData, setFormData] = useState(existingTransaction || { type: "income", category: "", amount: "", date: "" });
  const addTransaction = useAddTransaction();
  const updateTransaction = useEditTransaction();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    if (existingTransaction) {
      await updateTransaction.mutateAsync({ id: existingTransaction.id, data: formData });
    } else {
      await addTransaction.mutateAsync(formData);
    }
    onClose();
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded bg-white">
      <label className="block mb-2">Type</label>
      <select value={formData.type} onChange={(e) => setFormData({ ...formData, type: e.target.value })} className="w-full p-2 border rounded">
        <option value="income">Income</option>
        <option value="expense">Expense</option>
      </select>

      <label className="block mt-2 mb-2">Category</label>
      <input type="text" value={formData.category} onChange={(e) => setFormData({ ...formData, category: e.target.value })} className="w-full p-2 border rounded" />

      <label className="block mt-2 mb-2">Amount</label>
      <input type="number" value={formData.amount} onChange={(e) => setFormData({ ...formData, amount: e.target.value })} className="w-full p-2 border rounded" />

      <label className="block mt-2 mb-2">Date</label>
      <input type="date" value={formData.date} onChange={(e) => setFormData({ ...formData, date: e.target.value })} className="w-full p-2 border rounded" />

      <button type="submit" className="mt-4 w-full bg-blue-500 text-white p-2 rounded">
        {existingTransaction ? "Update Transaction" : "Add Transaction"}
      </button>
    </form>
  );
};

export default TransactionForm;
