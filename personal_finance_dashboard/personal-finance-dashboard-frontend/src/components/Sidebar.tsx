import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="w-64 h-screen bg-gray-800 text-white flex flex-col p-5">
      <h2 className="text-xl font-semibold mb-6">Finance Dashboard</h2>
      <nav className="flex flex-col space-y-4">
        <Link to="/" className="hover:text-blue-400">Dashboard</Link>
        <Link to="/transactions" className="hover:text-blue-400">Transactions</Link>
        <Link to="/net-worth" className="hover:text-blue-400">Net Worth</Link>
      </nav>
    </div>
  );
};

export default Sidebar;
