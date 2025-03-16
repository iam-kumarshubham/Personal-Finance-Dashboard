import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const IncomeVsExpensesChart = ({ data }: { data: any }) => {
  const chartData = {
    labels: data.map((entry: any) => entry.month),
    datasets: [
      {
        label: "Income",
        data: data.map((entry: any) => entry.income),
        borderColor: "green",
        backgroundColor: "rgba(0, 128, 0, 0.2)",
        tension: 0.3,
      },
      {
        label: "Expenses",
        data: data.map((entry: any) => entry.expenses),
        borderColor: "red",
        backgroundColor: "rgba(255, 0, 0, 0.2)",
        tension: 0.3,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default IncomeVsExpensesChart;
