import math

spot_price = 140
strike_price = 100 
variance = 0.3   #30% 
time_period = 0.5   #0.5 years or 6 months 
risk_free_rate = 0.1  #10%

def BSM(d1,d2,spot_price,strike_price,risk_free_rate,time_period):
    CDF_Normal_d1 = cdf(d1)
    CDF_Normal_d2 = cdf(d2)
    actual_price_part = spot_price * CDF_Normal_d1
    adjusted_price_part = strike_price * math.exp(-risk_free_rate*time_period) * CDF_Normal_d2
    return actual_price_part - adjusted_price_part

def d1_function(spot_price, strike_price, risk_free_rate, time_period, variance):
    Numerator =  math.log(spot_price/strike_price) + (variance**2/2)*(time_period) + (risk_free_rate*time_period)
    Denominator = variance * math.sqrt(time_period)
    return Numerator/Denominator

def d2_function(spot_price, strike_price, risk_free_rate, time_period, variance):
    d1_value = d1_function(spot_price,strike_price,risk_free_rate,time_period, variance)
    return  d1_value - variance * math.sqrt(time_period)

def cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

d1 = d1_function(spot_price, strike_price, risk_free_rate, time_period, variance)
d2 = d2_function(spot_price, strike_price, risk_free_rate, time_period, variance)
value = BSM(d1,d2,spot_price,strike_price,risk_free_rate,time_period)
print(value)
