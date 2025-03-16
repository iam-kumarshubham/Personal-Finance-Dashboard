import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import NetWorth from "./pages/NetWorth";
import Login from "./pages/auth/Login";
import Signup from "./pages/auth/Signup";

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/transactions" element={<Transactions />} />
        <Route path="/net-worth" element={<NetWorth />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </div>
  );
}

export default App;
