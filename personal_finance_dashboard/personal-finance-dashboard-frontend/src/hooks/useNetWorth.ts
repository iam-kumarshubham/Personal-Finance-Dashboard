import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { getNetWorth, addNetWorthEntry, updateNetWorthEntry, deleteNetWorthEntry } from "../api/networth";

export const useNetWorth = () => {
  return useQuery({
    queryKey: ["networth"],
    queryFn: getNetWorth
  });
};

export const useAddNetWorthEntry = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: addNetWorthEntry,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["networth"] });
    },
  });
};

export const useUpdateNetWorthEntry = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, entry }: { id: string; entry: any }) => updateNetWorthEntry(id, entry),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["networth"] });
    },
  });
};

export const useDeleteNetWorthEntry = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: deleteNetWorthEntry,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["networth"] });
    },
  });
};
