import { useState } from "react";
import NetWorthList from "../components/NetWorthList";
import NetWorthForm from "../components/NetWorthForm";

const NetWorth = () => {
  const [showForm, setShowForm] = useState(false);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Net Worth</h1>
      <button onClick={() => setShowForm(true)} className="mb-4 bg-green-500 text-white p-2 rounded">
        Add Net Worth Entry
      </button>

      {showForm && <NetWorthForm onClose={() => setShowForm(false)} />}
      <NetWorthList />
    </div>
  );
};

export default NetWorth;
