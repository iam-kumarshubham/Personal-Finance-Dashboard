import { Line } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const NetWorthChart = ({ data }: { data: any }) => {
  const chartData = {
    labels: data.map((entry: any) => entry.date),
    datasets: [
      {
        label: "Net Worth",
        data: data.map((entry: any) => entry.assets - entry.liabilities),
        borderColor: "blue",
        backgroundColor: "rgba(0, 0, 255, 0.2)",
        tension: 0.3,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default NetWorthChart;
