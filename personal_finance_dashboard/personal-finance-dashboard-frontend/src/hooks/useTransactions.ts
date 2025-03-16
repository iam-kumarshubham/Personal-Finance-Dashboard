import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import {
  getTransactions,
  addTransaction,
  editTransaction,
  deleteTransaction,
} from "../api/transactions";

// Fetch transactions
export const useTransactions = () => {
  return useQuery({
    queryKey: ["transactions"],
    queryFn: getTransactions,
  });
};

// Add transaction
export const useAddTransaction = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: addTransaction,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["transactions"] });
    },
  });
};

export const useEditTransaction = () => {
    const queryClient = useQueryClient();
    return useMutation({
      mutationFn: ({ id, data }: { id: string; data: any }) =>
        editTransaction(id, data),
      onSuccess: () => {
        queryClient.invalidateQueries({ queryKey: ["transactions"]});
      },
    });
  };

// Delete transaction
export const useDeleteTransaction = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: deleteTransaction,
    onSuccess: () => {
      queryClient.invalidateQueries({queryKey: ["transactions"]});
    },
  });
};
