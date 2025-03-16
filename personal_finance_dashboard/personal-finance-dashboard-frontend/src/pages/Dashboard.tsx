import { useState, useEffect } from "react";
import IncomeVsExpensesChart from "../components/charts/IncomeVsExpensesChart";
import NetWorthChart from "../components/charts/NetWorthChart";
import ExpenseBreakdownChart from "../components/charts/ExpenseBreakdownChart";
import { getTransactions } from "../api/transactions";
import { getNetWorth } from "../api/networth";

const Dashboard = () => {
  const [incomeExpensesData, setIncomeExpensesData] = useState<{ month: string; income: number; expenses: number }[]>([]);
  const [netWorthData, setNetWorthData] = useState<{ date: string; value: number }[]>([]);
  const [expenseBreakdownData, setExpenseBreakdownData] = useState<{ category: string; amount: number }[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const transactions = await getTransactions();
      const netWorth = await getNetWorth();

      // Process income vs. expenses (last 6 months)
      const incomeExpenses = processIncomeExpenses(transactions);
      setIncomeExpensesData(incomeExpenses);

      // Process net worth trend
      setNetWorthData(netWorth);

      // Process expense breakdown
      const expenses = transactions.filter((t: any) => t.type === "expense");
      const breakdown = processExpenseBreakdown(expenses);
      setExpenseBreakdownData(breakdown);
    };

    fetchData();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="p-4 border rounded bg-white">
          <h2 className="text-lg font-bold">Income vs. Expenses (Last 6 Months)</h2>
          <IncomeVsExpensesChart data={incomeExpensesData} />
        </div>

        <div className="p-4 border rounded bg-white">
          <h2 className="text-lg font-bold">Net Worth Trend</h2>
          <NetWorthChart data={netWorthData} />
        </div>

        <div className="p-4 border rounded bg-white col-span-2">
          <h2 className="text-lg font-bold">Expense Breakdown</h2>
          <ExpenseBreakdownChart data={expenseBreakdownData} />
        </div>
      </div>
    </div>
  );
};

// Helper function to process transactions for income vs. expenses chart
const processIncomeExpenses = (transactions: any): { month: string; income: number; expenses: number }[] => {
  const groupedData: any = {};
  
  transactions.forEach((t: any) => {
    const month = new Date(t.date).toLocaleString("default", { month: "short" });
    if (!groupedData[month]) {
      groupedData[month] = { month, income: 0, expenses: 0 };
    }
    if (t.type === "income") groupedData[month].income += t.amount;
    else groupedData[month].expenses += t.amount;
  });

  return Object.values(groupedData);
};

// Helper function to process transactions for expense breakdown chart
const processExpenseBreakdown = (transactions: any): { category: string; amount: number }[] => {
  const groupedData: any = {};

  transactions.forEach((t: any) => {
    if (!groupedData[t.category]) groupedData[t.category] = { category: t.category, amount: 0 };
    groupedData[t.category].amount += t.amount;
  });

  return Object.values(groupedData);
};

export default Dashboard;
