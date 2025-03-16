import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login"); // Redirect to login after logout
  };

  return (
    <nav className="flex justify-between p-4 bg-gray-900 text-white">
      <h1 className="text-lg font-bold">Finance Dashboard</h1>
      <button onClick={handleLogout} className="bg-red-500 px-4 py-2 rounded">
        Logout
      </button>
    </nav>
  );
};

export default Navbar;
  
