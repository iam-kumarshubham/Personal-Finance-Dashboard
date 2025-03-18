import React, { useEffect, useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ChartOptions,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import { charts, IncomeExpenseData, DateRange } from '../../api/charts';
import DateRangeSelector from '../common/DateRangeSelector';
import { format, subMonths } from 'date-fns';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options: ChartOptions<'bar'> = {
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      position: 'top' as const,
    },
    title: {
      display: false,
    },
    tooltip: {
      callbacks: {
        label: (context) => {
          const value = context.raw as number;
          return `${context.dataset.label}: $${value.toLocaleString()}`;
        },
      },
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

const IncomeExpenseChart: React.FC = () => {
  const [dateRange, setDateRange] = useState<DateRange>({
    startDate: format(subMonths(new Date(), 6), 'yyyy-MM-dd'),
    endDate: format(new Date(), 'yyyy-MM-dd'),
  });
  const [data, setData] = useState<IncomeExpenseData[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await charts.getIncomeExpense(dateRange);
        setData(response);
      } catch (err) {
        setError('Failed to fetch income and expense data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [dateRange]);

  const chartData = {
    labels: data.map((item) => format(new Date(item.date), 'MMM d')),
    datasets: [
      {
        label: 'Income',
        data: data.map((item) => item.income),
        backgroundColor: 'rgba(34, 197, 94, 0.5)',
        borderColor: 'rgb(34, 197, 94)',
        borderWidth: 1,
      },
      {
        label: 'Expenses',
        data: data.map((item) => item.expenses),
        backgroundColor: 'rgba(239, 68, 68, 0.5)',
        borderColor: 'rgb(239, 68, 68)',
        borderWidth: 1,
      },
    ],
  };

  if (loading) {
    return (
      <div className="h-full w-full flex items-center justify-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="h-full w-full flex items-center justify-center text-red-600">
        {error}
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <DateRangeSelector value={dateRange} onChange={setDateRange} />
      <div className="h-64">
        <Bar options={options} data={chartData} />
      </div>
    </div>
  );
};

export default IncomeExpenseChart; 