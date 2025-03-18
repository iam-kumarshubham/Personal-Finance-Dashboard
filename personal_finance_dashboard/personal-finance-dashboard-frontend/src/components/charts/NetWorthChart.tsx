import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'top' as const,
    },
    title: {
      display: false,
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        callback: (value: number) => `$${value.toLocaleString()}`,
      },
    },
  },
};

const labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];

const data = {
  labels,
  datasets: [
    {
      label: 'Net Worth',
      data: [25000, 28000, 30000, 32000, 35000, 30000],
      borderColor: 'rgb(99, 102, 241)',
      backgroundColor: 'rgba(99, 102, 241, 0.5)',
      tension: 0.4,
      fill: true,
    },
  ],
};

const NetWorthChart: React.FC = () => {
  return (
    <div className="h-full w-full">
      <Line options={options} data={data} />
    </div>
  );
};

export default NetWorthChart;
