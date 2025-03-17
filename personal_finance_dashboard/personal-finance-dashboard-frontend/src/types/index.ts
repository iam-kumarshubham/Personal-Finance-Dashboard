export type TransactionType = 'income' | 'expense';

export interface Transaction {
  id: number;
  user_id: number;
  type: TransactionType;
  category: string;
  amount: number;
  description?: string;
  date: string;
  created_at: string;
  updated_at?: string;
}

export type AssetType = 'bank' | 'investment' | 'property' | 'other';

export interface Asset {
  id: number;
  user_id: number;
  name: string;
  type: AssetType;
  value: number;
  description?: string;
  created_at: string;
  updated_at?: string;
}

export type LiabilityType = 'loan' | 'credit_card' | 'mortgage' | 'other';

export interface Liability {
  id: number;
  user_id: number;
  name: string;
  type: LiabilityType;
  value: number;
  description?: string;
  created_at: string;
  updated_at?: string;
}

export interface NetWorth {
  total_assets: number;
  total_liabilities: number;
  net_worth: number;
}

export interface User {
  id: number;
  email: string;
  full_name: string;
  created_at: string;
  updated_at?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface SignUpCredentials extends LoginCredentials {
  full_name: string;
} 