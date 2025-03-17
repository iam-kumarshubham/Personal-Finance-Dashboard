import { supabase } from "../services/supabase";

export const fetchTransactions = async () => {
  const { data, error } = await supabase.from("transactions").select("*");
  if (error) throw error;
  return data;
};

export const addTransaction = async (transaction: {
  type: string;
  category: string;
  amount: number;
}) => {
  const { data, error } = await supabase.from("transactions").insert([transaction]);
  if (error) throw error;
  return data;
};

export const deleteTransaction = async (id: number) => {
  const { error } = await supabase.from("transactions").delete().eq("id", id);
  if (error) throw error;
};

export const updateTransaction = async (id: number, updatedData: any) => {
  const { data, error } = await supabase.from("transactions").update(updatedData).eq("id", id);
  if (error) throw error;
  return data;
};
