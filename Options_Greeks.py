import math

def cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

# considering the stnadard normal distribution with mean=0 and variance=1
def pdf(x):
    return math.exp(-x**2/2) / math.sqrt(2*math.pi)

def d1_function(spot_price, strike_price, risk_free_rate, time_period, variance):
    Numerator =  math.log(spot_price/strike_price) + (variance**2/2)*(time_period) + (risk_free_rate*time_period)
    Denominator = variance * math.sqrt(time_period)
    return Numerator/Denominator

def d2_function(spot_price, strike_price, risk_free_rate, time_period, variance):
    d1_value = d1_function(spot_price,strike_price,risk_free_rate,time_period, variance)
    return  d1_value - variance * math.sqrt(time_period)

def delta(spot_price, strike_price, risk_free_rate, time_period, variance, option_type):
    if option_type == 'call':
        d1 = d1_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        delta = cdf(d1)
    elif option_type == 'put':
        d1 = d1_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        delta = -cdf(-d1)
    return delta

# Gamma is same for both call and put options 
def gamma(spot_price, strike_price, risk_free_rate, time_period, variance, option_type):
    if option_type == 'call' or option_type == 'put':
        d1 = d1_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        # Using pdf as to calculate the gamma, we use the derivative of cdf of d1
        # We know that the derivative of cdf is the pdf
        numerator = pdf(d1)
        denominator = spot_price * variance * math.sqrt(time_period)
        gamma = numerator / denominator
    return gamma
    
def theta(spot_price, strike_price, risk_free_rate, time_period, variance, option_type):
    # Using pdf as to calculate the theta, we use the derivative of cdf of d1
    # We know that the derivative of cdf is the pdf
    pdf_d1 = pdf(d1_function(spot_price, strike_price, risk_free_rate, time_period, variance))
    numerator_one = - spot_price * variance * pdf_d1
    denominator_one = 2 * math.sqrt(time_period)
    first_term = numerator_one/denominator_one
    if option_type == 'call':
        d2_value = d2_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        second_term = -risk_free_rate * strike_price * math.exp(-risk_free_rate*time_period) * cdf(d2_value)
        theta = first_term + second_term
    elif option_type == 'put':
        d2_value = d2_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        second_term = risk_free_rate * strike_price * math.exp(-risk_free_rate*time_period) * cdf(-d2_value)
        theta = first_term + second_term
    return theta/365  #We divide by 365 to get the value in trading days

# Vega is same for both call and put options 
def vega(spot_price, strike_price, risk_free_rate, time_period, variance, option_type):
    # Using pdf as to calculate the vega, we use the derivative of cdf of d1
    # We know that the derivative of cdf is the pdf
    pdf_d1 = pdf(d1_function(spot_price, strike_price, risk_free_rate, time_period, variance)) 
    if option_type == 'call' or option_type == 'put':
        vega = spot_price * math.exp(-risk_free_rate * time_period) * math.sqrt(time_period) * pdf_d1
    vega = vega/100  # We divide by 100 to remove the percentage
    return vega

def rho(spot_price, strike_price, risk_free_rate, time_period, variance, option_type):
    if option_type == 'call':
        d2_value = d2_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        rho = strike_price * time_period * math.exp(-risk_free_rate * time_period) * cdf(d2_value)
    elif option_type == 'put':
        d2_value = d2_function(spot_price, strike_price, risk_free_rate, time_period, variance)
        rho = - strike_price * time_period * math.exp(-risk_free_rate * time_period) * cdf(-d2_value)
    return rho/100  #We divide by 100 to remove the percentage