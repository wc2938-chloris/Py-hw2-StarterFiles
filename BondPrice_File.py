import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    coupon = face * couponRate
    
    periods = np.arange(1,((m * ppy)+1))
    pvcf = np.full(m * ppy, coupon)
    pvcf[-1] += face
    
    bondPrice = np.sum(pvcf / (1 + y / ppy) ** periods)
    
    return(bondPrice)

print(getBondPrice(0.03,2000000,0.04,10,1))


