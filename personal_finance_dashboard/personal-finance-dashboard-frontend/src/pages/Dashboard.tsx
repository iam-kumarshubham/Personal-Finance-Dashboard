import React, { useEffect, useState } from 'react';
import DashboardLayout from '../layouts/DashboardLayout';
import NetWorthChart from '../components/charts/NetWorthChart';
import IncomeExpenseChart from '../components/charts/IncomeExpenseChart';
import { charts, ChartSummary } from '../api/charts';
import { formatCurrency, formatPercentage } from '../utils/formatters';

const Dashboard: React.FC = () => {
  const [summary, setSummary] = useState<ChartSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        setLoading(true);
        const data = await charts.getSummary();
        setSummary(data);
      } catch (err) {
        setError('Failed to fetch dashboard summary');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchSummary();
  }, []);

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex items-center justify-center h-full">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
        </div>
      </DashboardLayout>
    );
  }

  if (error || !summary) {
    return (
      <DashboardLayout>
        <div className="flex items-center justify-center h-full text-red-600">
          {error || 'No data available'}
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-6">
        {/* Page Header */}
        <div>
          <h1 className="text-2xl font-semibold text-gray-900">Dashboard Overview</h1>
          <p className="mt-1 text-sm text-gray-500">
            Welcome back! Here's what's happening with your finances.
          </p>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Total Assets</p>
                <p className="mt-2 text-3xl font-semibold text-gray-900">
                  {formatCurrency(summary.totalAssets)}
                </p>
              </div>
              <div className="p-3 bg-green-50 rounded-full">
                <span className="text-green-600 text-xl">💰</span>
              </div>
            </div>
            <div className="mt-4">
              <div className="flex items-center text-sm">
                <span className={summary.assetChange >= 0 ? 'text-green-600' : 'text-red-600'}>
                  {formatPercentage(summary.assetChange)}
                </span>
                <span className="text-gray-500 ml-2">from last month</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Total Liabilities</p>
                <p className="mt-2 text-3xl font-semibold text-gray-900">
                  {formatCurrency(summary.totalLiabilities)}
                </p>
              </div>
              <div className="p-3 bg-red-50 rounded-full">
                <span className="text-red-600 text-xl">📝</span>
              </div>
            </div>
            <div className="mt-4">
              <div className="flex items-center text-sm">
                <span className={summary.liabilityChange <= 0 ? 'text-green-600' : 'text-red-600'}>
                  {formatPercentage(summary.liabilityChange)}
                </span>
                <span className="text-gray-500 ml-2">from last month</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Net Worth</p>
                <p className="mt-2 text-3xl font-semibold text-gray-900">
                  {formatCurrency(summary.netWorth)}
                </p>
              </div>
              <div className="p-3 bg-blue-50 rounded-full">
                <span className="text-blue-600 text-xl">📊</span>
              </div>
            </div>
            <div className="mt-4">
              <div className="flex items-center text-sm">
                <span className={summary.netWorthChange >= 0 ? 'text-green-600' : 'text-red-600'}>
                  {formatPercentage(summary.netWorthChange)}
                </span>
                <span className="text-gray-500 ml-2">from last month</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">Monthly Income</p>
                <p className="mt-2 text-3xl font-semibold text-gray-900">
                  {formatCurrency(summary.monthlyIncome)}
                </p>
              </div>
              <div className="p-3 bg-purple-50 rounded-full">
                <span className="text-purple-600 text-xl">💸</span>
              </div>
            </div>
            <div className="mt-4">
              <div className="flex items-center text-sm">
                <span className={summary.incomeChange >= 0 ? 'text-green-600' : 'text-red-600'}>
                  {formatPercentage(summary.incomeChange)}
                </span>
                <span className="text-gray-500 ml-2">from last month</span>
              </div>
            </div>
          </div>
        </div>

        {/* Charts Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Net Worth Trend</h2>
            <NetWorthChart />
          </div>

          <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Income vs Expenses</h2>
            <IncomeExpenseChart />
          </div>
        </div>

        {/* Recent Transactions */}
        <div className="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Recent Transactions</h2>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead>
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Description
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Category
                  </th>
                  <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Amount
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                <tr>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Mar 17, 2024
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    Salary
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Income
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-right text-green-600">
                    +$5,000
                  </td>
                </tr>
                <tr>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Mar 16, 2024
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    Groceries
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Food
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-right text-red-600">
                    -$150
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;
