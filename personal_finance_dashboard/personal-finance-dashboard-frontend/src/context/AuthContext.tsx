import React, { createContext, useContext, useState, useEffect } from 'react';
import { User, LoginCredentials, SignUpCredentials } from '../types';
import { auth } from '../api/client';

interface AuthContextType {
  user: User | null;
  loading: boolean;
  error: string | null;
  login: (credentials: LoginCredentials) => Promise<void>;
  signup: (credentials: SignUpCredentials) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      auth.getCurrentUser()
        .then(setUser)
        .catch(() => {
          localStorage.removeItem('token');
          setUser(null);
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  const login = async (credentials: LoginCredentials) => {
    try {
      setLoading(true);
      setError(null);
      await auth.login(credentials);
      const user = await auth.getCurrentUser();
      setUser(user);
    } catch (err) {
      setError('Invalid email or password');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const signup = async (credentials: SignUpCredentials) => {
    try {
      setLoading(true);
      setError(null);
      await auth.signup(credentials);
      await login({ email: credentials.email, password: credentials.password });
    } catch (err) {
      setError('Failed to create account');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    setError(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, error, login, signup, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
