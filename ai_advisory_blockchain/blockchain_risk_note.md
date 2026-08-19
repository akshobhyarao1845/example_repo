# Blockchain / Crypto Risk Note

A retail-facing Paytm Crypto Insights feature would need strong controls around stablecoin type, reserve transparency, redemption mechanics, smart-contract risk, and governance. Fiat-collateralized stablecoins are generally easier to reason about than algorithmic designs because their intended value is tied to identifiable reserves, but reserve quality, custody, liquidity and redemption concentration still matter. Algorithmic stablecoins can embed reflexive tokenomics and feedback loops that amplify de-pegging risk.

DeFi and DAO exposure adds another layer: governance concentration, anonymous voting power, upgrade keys, oracle dependencies, bridge risk, liquidity incentives and smart-contract vulnerabilities can turn an apparently diversified token into a highly correlated technology and governance bet. A retail watchlist should therefore expose risk labels, reserve/governance information, material warnings and stale-data indicators rather than presenting a single simplistic risk score.

For a retail advisory product, my recommendation is a maximum crypto allocation of **2%** of investable assets, with a default of zero for investors who cannot tolerate a complete loss. CAPM alone is not a sufficient reason to include crypto: many crypto assets lack dividends or conventional intrinsic cash flows, while observed returns can be heavy-tailed and positively skewed. Low or unstable correlation with traditional assets may provide diversification at times, but survivorship bias, high transaction costs, regime changes and severe drawdowns weaken a naive mean-variance argument. A small capped allocation therefore treats crypto as a speculative satellite position rather than a core holding.

## T.A.N.G. fraud vectors

**Authority + Temptation:** an attacker impersonates a bank, platform employee or regulator and pressures a user to approve a UPI payment, share an OTP, or move money to a “safe” account. A bank-side real-time defense is transaction-risk scoring with step-up authentication and an explicit cooling-off/interruption for unusual beneficiary, device and amount combinations.

**Need + Greed:** an attacker exploits urgent credit needs or promises unusually high investment returns, then uses a fake lending/investment workflow to collect credentials or induce transfers. A bank-side defense is beneficiary and transaction anomaly detection combined with scam-pattern intelligence, warning screens, and rapid transaction holds/review when the behavioural pattern is inconsistent with the customer’s history.
