from scipy.stats import norm

def ei(mean, std, target):
    if std <= 0:
        return 0.0  
    else:
        z = (mean - target) / std
        return std * (norm.pdf(z) + z * norm.cdf(z))