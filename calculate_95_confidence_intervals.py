# calculates 95% confidence intervals using wilson score interval
import statsmodels.api as statsmodels

true_positive= [165, 146, 123, 107, 89, 67, 51, 38, 19]
false_negative= [115, 96, 95, 77, 64, 50, 40, 24, 14]
false_positive= [15, 14, 10, 10, 10, 7, 5, 4, 4]
true_negative= [2204, 1965, 1716, 1472, 1225, 987, 737, 490, 241]

for i in range(9):
    print('Specificity:',
          statsmodels.stats.proportion_confint(true_negative[i], true_negative[i] + false_positive[i], alpha=0.05, method='wilson'))
    print('Sensitivity:',
          statsmodels.stats.proportion_confint(true_positive[i], true_positive[i] + false_negative[i], alpha=0.05, method='wilson'))