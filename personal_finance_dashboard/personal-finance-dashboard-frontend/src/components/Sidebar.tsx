import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside className="w-64 bg-white shadow-lg h-screen p-5">
      <h2 className="text-xl font-bold mb-6">Finance Dashboard</h2>
      <nav>
        <ul className="space-y-4">
          <li>
            <Link to="/dashboard" className="block p-2 text-gray-700 hover:bg-gray-200 rounded">
              📊 Dashboard
            </Link>
          </li>
          <li>
            <Link to="/transactions" className="block p-2 text-gray-700 hover:bg-gray-200 rounded">
              💰 Transactions
            </Link>
          </li>
          <li>
            <Link to="/net-worth" className="block p-2 text-gray-700 hover:bg-gray-200 rounded">
              🏦 Net Worth
            </Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
