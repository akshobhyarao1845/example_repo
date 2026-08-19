import re
def extract_signals(snippet):
 s=snippet.lower(); risk=[]
 if 'litigation' in s:risk.append('litigation')
 if 'regulatory' in s:risk.append('regulatory')
 if re.search(r'top three customers|customer concentration|account for approximately',s):risk.append('customer concentration')
 hedge=any(x in s for x in ['assuming','cautiously','visibility']); sentiment='confident' if ('confident' in s or 'approved' in s) else ('cautious' if hedge else 'neutral'); return {'risk_flags':risk,'hedging_detected':hedge,'sentiment':sentiment}
if __name__=='__main__':
 from disclosure_snippets import DISCLOSURE_SNIPPETS
 for x in DISCLOSURE_SNIPPETS: print(x,extract_signals(x))
