import { supabase } from "../services/supabase";

export const fetchNetWorth = async () => {
  const { data: assetsData, error: assetsError } = await supabase.from("assets").select("*");
  const { data: liabilitiesData, error: liabilitiesError } = await supabase.from("liabilities").select("*");

  if (assetsError || liabilitiesError) throw new Error("Error fetching net worth data");

  const assets = assetsData.reduce((acc, item) => acc + item.amount, 0);
  const liabilities = liabilitiesData.reduce((acc, item) => acc + item.amount, 0);
  return { assets, liabilities, netWorth: assets - liabilities };
};
