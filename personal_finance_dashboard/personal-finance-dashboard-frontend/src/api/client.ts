import axios from 'axios';
import { AuthResponse, LoginCredentials, SignUpCredentials, User, Transaction, Asset, Liability, NetWorth } from '../types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if it exists
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth endpoints
export const auth = {
  login: async (credentials: LoginCredentials): Promise<AuthResponse> => {
    const response = await apiClient.post<AuthResponse>('/auth/login', credentials);
    localStorage.setItem('token', response.data.access_token);
    return response.data;
  },

  signup: async (credentials: SignUpCredentials): Promise<User> => {
    const response = await apiClient.post<User>('/auth/signup', credentials);
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await apiClient.get<User>('/auth/me');
    return response.data;
  },
};

// Transaction endpoints
export const transactions = {
  getAll: async (): Promise<Transaction[]> => {
    const response = await apiClient.get<Transaction[]>('/transactions');
    return response.data;
  },

  create: async (transaction: Omit<Transaction, 'id' | 'user_id' | 'created_at' | 'updated_at'>): Promise<Transaction> => {
    const response = await apiClient.post<Transaction>('/transactions', transaction);
    return response.data;
  },

  update: async (id: number, transaction: Partial<Transaction>): Promise<Transaction> => {
    const response = await apiClient.put<Transaction>(`/transactions/${id}`, transaction);
    return response.data;
  },

  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/transactions/${id}`);
  },

  getSummary: async (): Promise<{ total_income: number; total_expenses: number; net_income: number }> => {
    const response = await apiClient.get('/transactions/summary');
    return response.data;
  },
};

// Asset endpoints
export const assets = {
  getAll: async (): Promise<Asset[]> => {
    const response = await apiClient.get<Asset[]>('/assets');
    return response.data;
  },

  create: async (asset: Omit<Asset, 'id' | 'user_id' | 'created_at' | 'updated_at'>): Promise<Asset> => {
    const response = await apiClient.post<Asset>('/assets', asset);
    return response.data;
  },

  update: async (id: number, asset: Partial<Asset>): Promise<Asset> => {
    const response = await apiClient.put<Asset>(`/assets/${id}`, asset);
    return response.data;
  },

  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/assets/${id}`);
  },

  getTotal: async (): Promise<number> => {
    const response = await apiClient.get<number>('/assets/total');
    return response.data;
  },
};

// Liability endpoints
export const liabilities = {
  getAll: async (): Promise<Liability[]> => {
    const response = await apiClient.get<Liability[]>('/liabilities');
    return response.data;
  },

  create: async (liability: Omit<Liability, 'id' | 'user_id' | 'created_at' | 'updated_at'>): Promise<Liability> => {
    const response = await apiClient.post<Liability>('/liabilities', liability);
    return response.data;
  },

  update: async (id: number, liability: Partial<Liability>): Promise<Liability> => {
    const response = await apiClient.put<Liability>(`/liabilities/${id}`, liability);
    return response.data;
  },

  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/liabilities/${id}`);
  },

  getTotal: async (): Promise<number> => {
    const response = await apiClient.get<number>('/liabilities/total');
    return response.data;
  },
};

// Net worth endpoint
export const netWorth = {
  getNetWorth: async (): Promise<NetWorth> => {
    const response = await apiClient.get<NetWorth>('/net-worth');
    return response.data;
  },
}; 