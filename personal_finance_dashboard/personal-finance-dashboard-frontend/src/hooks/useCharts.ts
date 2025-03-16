import { useQuery } from "@tanstack/react-query";
import { getIncomeExpenseTrends, getExpenseBreakdown } from "../api/charts";

// Fetch Income vs. Expense Trends
export const useIncomeExpenseTrends = () => {
  return useQuery({ queryKey: ["incomeExpenseTrends"], queryFn: getIncomeExpenseTrends });
};

// Fetch Expense Breakdown
export const useExpenseBreakdown = () => {
  return useQuery({ queryKey: ["expenseBreakdown"], queryFn: getExpenseBreakdown });
};
