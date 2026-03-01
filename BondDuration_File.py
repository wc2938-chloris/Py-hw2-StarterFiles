import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    pvcfsum = 0
    coupon = face * couponRate
    
    periods = np.arange(1,((m * ppy)+1))
    pvcf = np.full(m * ppy, coupon)
    pvcf[-1] += face
    
    pvcfsum = np.sum(pvcf / (1 + y / ppy) ** periods)
    
    bondDuration = np.sum(((periods / ppy) * pvcf / ((1 + y / ppy) ** periods)) / pvcfsum)
    
    return(bondDuration)

print(getBondDuration(0.03, 2000000, 0.05, 10, 1))
