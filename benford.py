import math
from scipy import stats

def calculate_benford_law(data):
    # Count the frequency of the first digit in the data
    digit_counts = [0] * 10
    for num in data:
        first_digit = int(str(abs(num))[0])
        digit_counts[first_digit] += 1
    
    # Calculate the expected frequency based on Benford's Law
    benford_freq = [0] * 10
    for i in range(1, 10):
        benford_freq[i] = math.log10(1 + 1/i) * len(data)
    
    # Calculate the chi-squared statistic and p-value
    chi2 = 0
    for i in range(1, 10):
        chi2 += (digit_counts[i] - benford_freq[i])**2 / benford_freq[i]
    p = 1 - stats.chi2.cdf(chi2, df=8)
    
    # Return the results as a dictionary
    results = {
        'digit_counts': digit_counts,
        'benford_freq': benford_freq,
        'chi2': chi2,
        'p': p
    }
    return results
