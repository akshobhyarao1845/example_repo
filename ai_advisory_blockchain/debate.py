from stock_universe import STOCK_UNIVERSE
def debate(ticker='PAYTECH'):
 d=STOCK_UNIVERSE[ticker]; bull=f"With an expected return of {d['analyst_expected_return']:.1%} against a beta of {d['beta']:.2f}, this offers attractive risk-adjusted upside."; bear=f"The {d['std_dev']:.1%} standard deviation signals meaningful volatility and downside risk."; synth=f"The bull case highlights the {d['analyst_expected_return']:.1%} reference return, while the bear case emphasizes {d['std_dev']:.1%} volatility. A balanced view is warranted given the beta of {d['beta']:.2f}."; return bull,bear,synth
if __name__=='__main__': print(*debate(),sep='\n')
