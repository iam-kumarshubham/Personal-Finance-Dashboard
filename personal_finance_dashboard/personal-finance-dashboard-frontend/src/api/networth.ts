import { supabase } from "../services/supabase";

// Fetch net worth data
export const getNetWorth = async () => {
  const { data, error } = await supabase
    .from("net_worth")
    .select("*")
    .order("date", { ascending: false });

  if (error) throw error;
  return data;
};

// Add a new net worth entry
export const addNetWorthEntry = async (entry: any) => {
  const { error } = await supabase.from("net_worth").insert([entry]);

  if (error) throw error;
};

// Update an existing net worth entry
export const updateNetWorthEntry = async (id: string, entry: any) => {
  const { error } = await supabase.from("net_worth").update(entry).eq("id", id);

  if (error) throw error;
};

// Delete a net worth entry
export const deleteNetWorthEntry = async (id: string) => {
  const { error } = await supabase.from("net_worth").delete().eq("id", id);

  if (error) throw error;
};
