export const formatCurrency = (value: number): string => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(value);
};

export const formatPercentage = (value: number): string => {
  const sign = value >= 0 ? '↑' : '↓';
  const formattedValue = Math.abs(value).toFixed(1);
  return `${sign} ${formattedValue}%`;
}; 