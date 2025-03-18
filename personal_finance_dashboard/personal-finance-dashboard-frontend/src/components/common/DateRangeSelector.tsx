import React from 'react';
import { format, subMonths, subDays, startOfDay, endOfDay } from 'date-fns';

export interface DateRange {
  startDate: string;
  endDate: string;
}

interface DateRangeSelectorProps {
  value: DateRange;
  onChange: (range: DateRange) => void;
}

const DateRangeSelector: React.FC<DateRangeSelectorProps> = ({ value, onChange }) => {
  const presets = [
    { label: 'Last 7 days', days: 7 },
    { label: 'Last 30 days', days: 30 },
    { label: 'Last 3 months', months: 3 },
    { label: 'Last 6 months', months: 6 },
    { label: 'Last year', months: 12 },
  ];

  const handlePresetClick = (days?: number, months?: number) => {
    const end = endOfDay(new Date());
    let start: Date;

    if (days) {
      start = startOfDay(subDays(end, days));
    } else if (months) {
      start = startOfDay(subMonths(end, months));
    } else {
      return;
    }

    onChange({
      startDate: format(start, 'yyyy-MM-dd'),
      endDate: format(end, 'yyyy-MM-dd'),
    });
  };

  return (
    <div className="flex items-center space-x-4">
      <div className="flex space-x-2">
        {presets.map((preset) => (
          <button
            key={preset.label}
            onClick={() => handlePresetClick(preset.days, preset.months)}
            className="px-3 py-1 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            {preset.label}
          </button>
        ))}
      </div>
      <div className="flex items-center space-x-2">
        <input
          type="date"
          value={value.startDate}
          onChange={(e) => onChange({ ...value, startDate: e.target.value })}
          className="px-3 py-1 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        />
        <span className="text-gray-500">to</span>
        <input
          type="date"
          value={value.endDate}
          onChange={(e) => onChange({ ...value, endDate: e.target.value })}
          className="px-3 py-1 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        />
      </div>
    </div>
  );
};

export default DateRangeSelector; 