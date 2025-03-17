const Navbar = () => {
  return (
    <div className="w-full bg-white shadow-md p-4 flex justify-between items-center">
      <h1 className="text-lg font-semibold">Dashboard</h1>
      <button className="bg-red-500 text-white px-4 py-2 rounded-lg">Logout</button>
    </div>
  );
};

export default Navbar;
