export type StrategyCounts = {
  cooperate?: number;
  defect?: number;
  tit_for_tat?: number;
  random?: number;
};

export type MetricsFrame = {
  type: "metrics" | "frame";
  generation: number;
  width?: number;
  height?: number;
  cooperation_ratio?: number;
  mean_payoff?: number;
  strategy_distribution?: StrategyCounts;
};

export function parseMetricsLine(line: string): MetricsFrame | null {
  try {
    const parsed = JSON.parse(line) as MetricsFrame;
    if (parsed.type !== "metrics" && parsed.type !== "frame") {
      return null;
    }
    return parsed;
  } catch {
    return null;
  }
}

