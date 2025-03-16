import { useState } from "react";
import { useAddNetWorthEntry, useUpdateNetWorthEntry } from "../hooks/useNetWorth";

const NetWorthForm = ({ existingEntry, onClose }: { existingEntry?: any; onClose: () => void }) => {
  const [formData, setFormData] = useState(existingEntry || { assets: "", liabilities: "", date: "" });
  const addNetWorthEntry = useAddNetWorthEntry();
  const updateNetWorthEntry = useUpdateNetWorthEntry();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    if (existingEntry) {
      await updateNetWorthEntry.mutateAsync(formData);
    } else {
      await addNetWorthEntry.mutateAsync(formData);
    }
    onClose();
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 border rounded bg-white">
      <label className="block mb-2">Assets</label>
      <input type="number" value={formData.assets} onChange={(e) => setFormData({ ...formData, assets: e.target.value })} className="w-full p-2 border rounded" />

      <label className="block mt-2 mb-2">Liabilities</label>
      <input type="number" value={formData.liabilities} onChange={(e) => setFormData({ ...formData, liabilities: e.target.value })} className="w-full p-2 border rounded" />

      <label className="block mt-2 mb-2">Date</label>
      <input type="date" value={formData.date} onChange={(e) => setFormData({ ...formData, date: e.target.value })} className="w-full p-2 border rounded" />

      <button type="submit" className="mt-4 w-full bg-blue-500 text-white p-2 rounded">
        {existingEntry ? "Update Entry" : "Add Entry"}
      </button>
    </form>
  );
};

export default NetWorthForm;
