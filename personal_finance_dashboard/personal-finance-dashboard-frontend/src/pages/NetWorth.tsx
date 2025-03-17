import { useEffect, useState } from "react";
import { fetchNetWorth } from "../api/networth";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

const NetWorth = () => {
  const [netWorthData, setNetWorthData] = useState({ assets: 0, liabilities: 0, netWorth: 0 });

  useEffect(() => {
    const getNetWorth = async () => {
      try {
        const data = await fetchNetWorth();
        setNetWorthData(data);
      } catch (error) {
        console.error("Error fetching net worth data:", error);
      }
    };

    getNetWorth();
  }, []);

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h2 className="text-2xl font-semibold my-4">Net Worth</h2>

        <div className="grid grid-cols-3 gap-4">
          <div className="bg-green-500 text-white p-4 rounded-lg shadow-md">
            <h3 className="text-lg">Total Assets</h3>
            <p className="text-xl font-bold">${netWorthData.assets}</p>
          </div>
          <div className="bg-red-500 text-white p-4 rounded-lg shadow-md">
            <h3 className="text-lg">Total Liabilities</h3>
            <p className="text-xl font-bold">${netWorthData.liabilities}</p>
          </div>
          <div className="bg-blue-500 text-white p-4 rounded-lg shadow-md">
            <h3 className="text-lg">Net Worth</h3>
            <p className="text-xl font-bold">${netWorthData.netWorth}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NetWorth;
