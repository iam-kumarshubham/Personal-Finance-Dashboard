import { PieChart, Pie, Tooltip, Cell, ResponsiveContainer } from "recharts";
import { useExpenseBreakdown } from "../hooks/useCharts";

const COLORS = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFDB33"];

const ExpensePieChart = () => {
  const { data, isLoading, error } = useExpenseBreakdown();

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading data.</p>;

  const formattedData = (data as { category: string; amount: number }[]).reduce((acc: any, item: any) => {
    const existing = acc.find((d: any) => d.category === item.category);
    if (existing) {
      existing.value += item.amount;
    } else {
      acc.push({ category: item.category, value: item.amount });
    }
    return acc;
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-lg font-bold mb-2">Expense Breakdown by Category</h2>
      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie data={formattedData} dataKey="value" nameKey="category" cx="50%" cy="50%" outerRadius={80}>
            {formattedData.map((_: any, index: number) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ExpensePieChart;
