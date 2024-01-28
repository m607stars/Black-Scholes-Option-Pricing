# Black-Scholes-Option-Pricing
This repository contains the pyhton implementation of Black Scholes model for both call and put options valuations
We need to input the following parmeters to get the call and put option valuation
* Spot price
* Strike price 
* Variance 
* Time Period 
* Risk free rate 

Option Greeks Calculations: 
Option Greeks are the derivatives of the pricing models. They give the rate of change of the option with respect to different parameters.
* Delta - It explains the rate of change of the option price with respect to the price of the underlying       security. It is the partial derivative of option price (Calculated by the Black Scholes model) w.r.t to the spot price
* Gamma - It explains the rate of change of delta with respect to the spot price. This implies that it is the second order partial derivative of the option price w.r.t the spot price
* Theta - It is the rate of change of the option price with respect to the time to maturity i.e. the time period before which the option will expire. Usually as the time to maturity decreases, the option balue also decreases. Theta is mathematically calculated as the partial derivative of the option price w.r.t. the time period.  
* Vega - It is the rate of change of the option price with respect to the volatility. It is the partial  derivative of the option price w.r.t the volatility. 

To Do Lists - 
* Implement the model in Excel
* Impement pricing charts