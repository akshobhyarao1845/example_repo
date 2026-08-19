import os, math
from stock_universe import STOCK_UNIVERSE,RISK_FREE_RATE,MARKET_RETURN
from investor_profiles import INVESTOR_PROFILES
ALLOC={'Conservative':['PAYBOND','PAYGOLD','PAYRETAIL'],'Moderate':['PAYRETAIL','PAYINFRA','PAYGOLD'],'Aggressive':['PAYTECH','PAYFIN','PAYINFRA']}
def get_stock_data(ticker): return STOCK_UNIVERSE[ticker]
def run_one(p):
 tickers=ALLOC[p['risk_tolerance']]; w=1/3; data=[get_stock_data(t) for t in tickers]; returns=[RISK_FREE_RATE+d['beta']*(MARKET_RETURN-RISK_FREE_RATE) for d in data]; port_ret=sum(returns)*w; var=sum(w*w*d['std_dev']**2 for d in data)+2*sum(w*w*.3*data[i]['std_dev']*data[j]['std_dev'] for i in range(3) for j in range(i+1,3)); vol=math.sqrt(var); status='ESCALATED_TO_HUMAN_ADVISOR' if vol>.20 else 'FINALIZED'; narrative=f"For {p['risk_tolerance']} investor {p['investor_id']}, we recommend an allocation across {', '.join(tickers)} with an expected portfolio return of {port_ret:.1%} and volatility of {vol:.1%}."; return {'investor_id':p['investor_id'],'tickers':tickers,'return':port_ret,'volatility':vol,'status':status,'narrative':narrative}
if __name__=='__main__':
 for p in INVESTOR_PROFILES: print(run_one(p))
