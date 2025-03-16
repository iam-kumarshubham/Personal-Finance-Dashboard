import { supabase } from "../services/supabase";

// Fetch all transactions
export const getTransactions = async () => {
  const { data, error } = await supabase
    .from("transactions")
    .select("*")
    .order("created_at", { ascending: false });

  if (error) throw error;
  return data;
};

// Add a new transaction
export const addTransaction = async (transaction: {
  title: string;
  amount: number;
  category: string;
  type: "income" | "expense";
}) => {
  const { data, error } = await supabase
    .from("transactions")
    .insert([transaction]);

  if (error) throw error;
  return data;
};

// Edit a transaction
export const editTransaction = async (id: string, updatedTransaction: any) => {
  const { data, error } = await supabase
    .from("transactions")
    .update(updatedTransaction)
    .eq("id", id);

  if (error) throw error;
  return data;
};

// Delete a transaction
export const deleteTransaction = async (id: string) => {
  const { error } = await supabase.from("transactions").delete().eq("id", id);

  if (error) throw error;
};
