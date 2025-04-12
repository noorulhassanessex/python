import statistics
import pandas as pd

def compute_statistics(data, grouped_df, frequency, midpoints):
    try:
        total_freq = sum(frequency)
        sum_fx = sum([f * m for f, m in zip(frequency, midpoints)])
        mean = sum_fx / total_freq

        median = statistics.median(data)
        try:
            mode = statistics.mode(data)
        except statistics.StatisticsError:
            mode = "Multiple Modes"

        variance = statistics.variance(data)
        std_dev = statistics.stdev(data)

        max_freq_index = frequency.index(max(frequency))
        modal_class = grouped_df.iloc[max_freq_index]['Classes']

        stats_df = pd.DataFrame({
            'Measure': ['Mean', 'Median', 'Mode', 'Variance', 'Standard Deviation', 'Modal Class'],
            'Value': [mean, median, mode, variance, std_dev, modal_class]
        })

        return stats_df

    except Exception as e:
        print(f"❌ Error in computing statistics: {e}")
        return pd.DataFrame()