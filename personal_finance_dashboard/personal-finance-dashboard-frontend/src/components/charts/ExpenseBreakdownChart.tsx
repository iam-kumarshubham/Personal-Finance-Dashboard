import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

const ExpenseBreakdownChart = ({ data }: { data: any }) => {
  const chartData = {
    labels: data.map((entry: any) => entry.category),
    datasets: [
      {
        label: "Expenses",
        data: data.map((entry: any) => entry.amount),
        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4CAF50", "#9966FF"],
      },
    ],
  };

  return <Pie data={chartData} />;
};

export default ExpenseBreakdownChart;
