import { supabase } from "../services/supabase";

// Fetch last 6 months' income & expense data
export const getIncomeExpenseTrends = async () => {
  const { data, error } = await supabase
    .from("transactions")
    .select("amount, type, date")
    .order("date", { ascending: false })
    .limit(6); // Fetch last 6 months

  if (error) throw error;
  return data;
};

// Fetch expense breakdown by category
export const getExpenseBreakdown = async () => {
  const { data, error } = await supabase
    .from("transactions")
    .select("category, amount")
    .eq("type", "expense");

  if (error) throw error;
  return data;
};
