import numpy as np
from scipy.stats import norm
import streamlit as st

st.title("Black Scholes Calculator")
 
# creates a horizontal line
st.write("---")

def black_scholes_calc(S0, K, r, T, sigma, option_type):
    '''This function calculates the value of the European option based on Black-Scholes formula'''
    # 1) determine N(d1) and N(d2)
    d1 = 1/(sigma*np.sqrt(T)) * (np.log(S0/K) + (r+sigma**2/2)*T)
    d2 = d1 - sigma*np.sqrt(T)
    nd1 = norm.cdf(d1)
    nd2 = norm.cdf(d2)
    n_d1 = norm.cdf(-d1)
    n_d2 = norm.cdf(-d2)
    # 2) determine call value
    c = nd1*S0 - nd2*K*np.exp(-r*T)
    # 3) determine put value
    p = K*np.exp(-r*T)*n_d2 - S0*n_d1
    # 4) define which value to return based on the option_type parameter
    if option_type=='call':
        st.success(c)
    elif option_type=='put':
        st.success(p)
    else:
        st.write('Wrong option type specified')

col1, col2 = st.columns(2, gap = 'large')
with col1:
    st.header('Enter input parameters')
    # input parameters
    S0 = st.number_input(label="Price of the underlying asset", value = 8)
    K = st.number_input(label="Strike price", value = 9)
    r = st.number_input(label="Interest rate", value = 0.01)
    T = st.number_input(label="Time to option expiration", value = 3/12)
    sigma = st.number_input(label="Volatility", value = 0.2)
    option_type = st.selectbox(
        'Option type',
        ('call', 'put'))
    if st.button("Calculate result"):
        black_scholes_calc(S0, K, r, T, sigma, option_type)
    
with col2:
    st.header('Step by step calculation')
    # d1
    st.latex(r'''d_1 = \frac{1}{\sigma\sqrt{T}} \left(\ln\left(\frac{S_0}{K}\right) + \left(r + \frac{\sigma^2}{2}\right)T\right)''')
    d1 = 1/(sigma*np.sqrt(T)) * (np.log(S0/K) + (r+sigma**2/2)*T)
    st.write(fr"d_1 = {d1}")
    # d2
    st.latex(r'''d_2 = d_1 - \sigma\sqrt{T}''')
    d2 = d1 - sigma*np.sqrt(T)
    st.write(f"d_2 = {d2}")
    # # N(d1)
    # st.latex(r'''N(d1) = \text{norm.cdf}(d1)''')
    nd1 = norm.cdf(d1)
    # st.write(f"N(d1) = {nd1}")   
    # # N(d2)
    # st.latex(r'''N(d2) = \text{norm.cdf}(d2)''') 
    nd2 = norm.cdf(d2)
    # st.write(f"N(d2) = {nd2}")   

    # # N(-d1)
    # st.latex(r'''N(-d1) = \text{norm.cdf}(-d1)''')
    n_d1 = norm.cdf(-d1)
    # st.write(f"N(-d1) = {n_d1}")

    # # N(-d2)
    # st.latex(r'''N(-d2) = \text{norm.cdf}(-d2)''')
    n_d2 = norm.cdf(-d2)
    # st.write(f"N(-d2) = {n_d2}")

    # Call Option Value (c)
    st.latex(r'''c = N(d_1)S_0 - N(d_2)Ke^{-rT}''')
    c = nd1*S0 - nd2*K*np.exp(-r*T)
    st.write(f"Call Option Value (c) = {c}")

    # Put Option Value (p)
    st.latex(r'''p = Ke^{-rT}N(-d_2) - S_0N(-d_1)''')
    p = K*np.exp(-r*T)*n_d2 - S0*n_d1
    st.write(f"Put Option Value (p) = {p}")








