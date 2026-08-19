def dcf(base_fcff=10000000,growth=.12,terminal_growth=.04,wacc=.11,years=5):
 if wacc-terminal_growth<.03: raise ValueError('Terminal growth must be at least 3pp below WACC')
 fcfs=[base_fcff*(1+growth)**i for i in range(1,years+1)]; tv=fcfs[-1]*(1+terminal_growth)/(wacc-terminal_growth); pv=sum(cf/(1+wacc)**i for i,cf in enumerate(fcfs,1))+tv/(1+wacc)**years; sens={}
 for dw in [-.01,0,.01]:
  for dg in [-.01,0,.01]: sens[(round((wacc+dw)*100,2),round((terminal_growth+dg)*100,2))]=fcfs[-1]*(1+terminal_growth+dg)/(wacc+dw-terminal_growth-dg)
 return fcfs,tv,pv,sens
if __name__=='__main__':
 print(dcf())
