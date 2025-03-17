import React, { useEffect, useState } from 'react';
import { SummaryCard } from '../components/SummaryCard';
import { RecentTransactions } from '../components/RecentTransactions';
import { transactions, netWorth } from '../api/client';
import { Transaction, NetWorth as NetWorthType } from '../types';

const Dashboard: React.FC = () => {
  const [netWorthData, setNetWorthData] = useState<NetWorthType | null>(null);
  const [recentTransactions, setRecentTransactions] = useState<Transaction[]>([]);
  const [transactionSummary, setTransactionSummary] = useState({
    total_income: 0,
    total_expenses: 0,
    net_income: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const [netWorthResponse, transactionsResponse, summaryResponse] = await Promise.all([
          netWorth.getNetWorth(),
          transactions.getAll(),
          transactions.getSummary(),
        ]);

        setNetWorthData(netWorthResponse);
        setRecentTransactions(transactionsResponse.slice(0, 5)); // Get only the 5 most recent transactions
        setTransactionSummary(summaryResponse);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        <SummaryCard
          title="Net Worth"
          value={netWorthData?.net_worth || 0}
          icon={<span className="text-white text-xl">💰</span>}
          color="bg-indigo-500"
        />
        <SummaryCard
          title="Total Assets"
          value={netWorthData?.total_assets || 0}
          icon={<span className="text-white text-xl">📈</span>}
          color="bg-green-500"
        />
        <SummaryCard
          title="Total Liabilities"
          value={netWorthData?.total_liabilities || 0}
          icon={<span className="text-white text-xl">📉</span>}
          color="bg-red-500"
        />
        <SummaryCard
          title="Net Income"
          value={transactionSummary.net_income}
          icon={<span className="text-white text-xl">💵</span>}
          color="bg-blue-500"
          trend={{
            value: transactionSummary.net_income,
            isPositive: transactionSummary.net_income >= 0,
          }}
        />
      </div>

      <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
        <div className="bg-white shadow rounded-lg p-6">
          <h3 className="text-lg leading-6 font-medium text-gray-900 mb-4">
            Income vs Expenses
          </h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between text-sm text-gray-500 mb-1">
                <span>Income</span>
                <span>{new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(transactionSummary.total_income)}</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-green-500 h-2 rounded-full"
                  style={{
                    width: `${(transactionSummary.total_income / (transactionSummary.total_income + transactionSummary.total_expenses)) * 100}%`,
                  }}
                ></div>
              </div>
            </div>
            <div>
              <div className="flex justify-between text-sm text-gray-500 mb-1">
                <span>Expenses</span>
                <span>{new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(transactionSummary.total_expenses)}</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-red-500 h-2 rounded-full"
                  style={{
                    width: `${(transactionSummary.total_expenses / (transactionSummary.total_income + transactionSummary.total_expenses)) * 100}%`,
                  }}
                ></div>
              </div>
            </div>
          </div>
        </div>

        <RecentTransactions transactions={recentTransactions} />
      </div>
    </div>
  );
};

export default Dashboard;
