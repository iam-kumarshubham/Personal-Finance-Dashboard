import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import { useIncomeExpenseTrends } from "../hooks/useCharts";

const IncomeExpenseChart = () => {
  const { data, isLoading, error } = useIncomeExpenseTrends() as { data: { date: string; type: string; amount: number }[]; isLoading: boolean; error: any };

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading data.</p>;

  const formattedData = data.map((item: any) => ({
    date: new Date(item.date).toLocaleDateString(),
    income: item.type === "income" ? item.amount : 0,
    expense: item.type === "expense" ? item.amount : 0,
  }));

  return (
    <div className="p-4">
      <h2 className="text-lg font-bold mb-2">Income vs Expenses (Last 6 Months)</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={formattedData}>
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <CartesianGrid stroke="#ccc" />
          <Line type="monotone" dataKey="income" stroke="#4CAF50" />
          <Line type="monotone" dataKey="expense" stroke="#FF5733" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default IncomeExpenseChart;
