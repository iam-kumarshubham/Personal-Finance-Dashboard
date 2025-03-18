import { apiClient } from './client';

export interface DateRange {
  startDate: string;
  endDate: string;
}

export interface NetWorthData {
  date: string;
  assets: number;
  liabilities: number;
  netWorth: number;
}

export interface IncomeExpenseData {
  date: string;
  income: number;
  expenses: number;
}

export interface ChartSummary {
  totalAssets: number;
  totalLiabilities: number;
  netWorth: number;
  monthlyIncome: number;
  monthlyExpenses: number;
  assetChange: number;
  liabilityChange: number;
  netWorthChange: number;
  incomeChange: number;
}

export const charts = {
  getNetWorthTrend: async (dateRange: DateRange): Promise<NetWorthData[]> => {
    const response = await apiClient.get<NetWorthData[]>('/charts/net-worth', {
      params: dateRange,
    });
    return response.data;
  },

  getIncomeExpense: async (dateRange: DateRange): Promise<IncomeExpenseData[]> => {
    const response = await apiClient.get<IncomeExpenseData[]>('/charts/income-expense', {
      params: dateRange,
    });
    return response.data;
  },

  getSummary: async (): Promise<ChartSummary> => {
    const response = await apiClient.get<ChartSummary>('/charts/summary');
    return response.data;
  },
};
