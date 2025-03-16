import { supabase } from "../services/supabase";
//import { supabase } from "../services/supabaseClient";

// Signup
export const signUp = async (email: string, password: string) => {
  const { data, error } = await supabase.auth.signUp({ email, password });
  if (error) throw error;
  return data.user;
};

// Login
export const login = async (email: string, password: string) => {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw error;
  return data.user;
};

// Logout
export const logout = async () => {
  await supabase.auth.signOut();
};

// Get current user
export const getUser = async () => {
  const { data: user } = await supabase.auth.getUser();
  return user;
};

