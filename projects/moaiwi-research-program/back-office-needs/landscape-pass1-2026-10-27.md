# Incumbent-tools & software-spend landscape — desk pass 1 (2026-10-27)

*First desk pass for T1/T2 (started per Brad, 2026-10-27: "you can begin the desk part of the project… helpful in formulating interview questions"). Feeds both plans and the R.1 interim landscape slice. **v0 — web-side only; all vendor/pricing claims unverified until the interviews.** URLs at the end.*

## Findings so far

1. **Generic searches drown in noise.** "Portfolio management software" returns project-portfolio-management and wealth-management listicles. The fund-specific landscape needs category-precise search terms: *private equity portfolio monitoring*, *fund accounting*, *impact measurement and management (IMM)*.
2. **A usable taxonomy exists (from a Masttro buyer's guide): GP-side vs. LP-side.** GP-side (monitor the companies inside the fund): Allvue, Chronograph, 73 Strings, Cobalt (FactSet), CEPRES. LP-side (track commitments across funds): Masttro, Addepar, Arch, Canoe Intelligence, FundCount, iLEVEL. Fund accounting / system of record: FundCount, Allvue, eFront. CRM/origination: DealCloud (Intapp), Navatar (Salesforce-native). VC-focused: Visible. The action-circle funds look LP-side + small-GP — **an interview question, not an assumption**.
3. **Pricing is quote-opaque.** No published prices in any of the buyer's guides ("not published, contact for a quote"). Consequence for T1: **the budget question is genuinely interview-only** on the vendor side; desk work can bound it (list prices for the SMB accounting layer, e.g. QuickBooks/Sage Intacct/Xero tiers are public) but cannot answer it.
4. **The impact-specific layer is thin and standards-shaped.** GIIN runs a "Data Platform Providers" program (IRIS+ metrics inside vendors' platforms) but **the partner list is JS-walled / not rendered** — needs another route (GIIN contacts, or the vendors' own sites claiming IRIS+ integration). UNEP-FI has a free Investment Portfolio Impact Analysis Tool (bank/PRB-oriented). Otherwise the IMM category is consultancies + templates + spreadsheets more than software — *to verify in interviews*.
5. **Standards division of labor (useful for the glossary and T5):** Common Approach states it plainly — *IRIS+ defines **what** to measure; the Common Impact Data Standard defines **how to share** it digitally.* IRIS+ also aligns "to more than 50 metrics frameworks, standards and platforms". Market-size claim from GIIN's own copy: impact investing = "USD 1.164 trillion industry" (rhetoric to treat as their framing, not our fact).
6. **The $20 budget holds so far** — this pass used search + fetch only; no LLM-generated synthesis billed beyond the session itself.

## Interview-question seeds (from this pass)

- Which of these tools do you actually run — portfolio monitoring (Chronograph/iLEVEL/Allvue/…), fund accounting (FundCount/Sage/QuickBooks), CRM (DealCloud/Salesforce), impact reporting (platform/consultant/spreadsheet)? What do you pay, per year?
- GP-side or LP-side — do you monitor portfolio-company KPIs yourselves? Who chases the data?
- How do you produce impact reports today (IRIS+ sets, theme reports, board packets)? Does any tool export to or align with IRIS+? Who does the mapping?
- What did you evaluate and reject? Why? What's renewal-time pain?
- What's still done in spreadsheets? What breaks at quarter-end?
- Research support: do you pay for research — subscriptions, consultants, or a person? (MOAIWI-4's "allocate budget for a person" remark — probe their framing.)
- What would make you switch, or add a subscription on top of what you have?

## Next steps (T1/T2 WPs)

- Job-postings scan (tool names in real reqs = ground-truth proxies) and G2/Capterra category pass; retry the GIIN partner list via vendor claims.
- Fold into the interview protocol (WP2) with Nic and Rachel; carry to the circle.

## URLs

- https://masttro.com/insights/private-equity-portfolio-monitoring-software (GP/LP taxonomy; names)
- https://fundcount.com/top-7-private-equity-portfolio-monitoring-software (buyer's guide; categories)
- https://www.lumonic.com/for-ai/best-private-equity-portfolio-monitoring-software-2026 (Chronograph/Cobalt/iLEVEL detail)
- https://www.chronograph.pe (vendor; portfolio monitoring)
- https://agorareal.com/compare/best-private-equity-portfolio-management-software (DealCloud/Navatar/Visible; pricing opacity)
- https://iris.thegiin.org/partners (IRIS+ Data Platform Providers — JS-walled, list not rendered)
- https://iris.thegiin.org/about and https://iris.thegiin.org/metrics (IRIS+ scope; "50+ frameworks" claim)
- https://www.commonapproach.org/knowledge/resources/how-giins-iris-and-common-approach-are-complementary ("what to measure" vs. "how to share")
- https://www.unepfi.org/impact/unep-fi-impact-analysis-tools/investment-portfolio-impact-analysis-tool
- https://startupstash.com/investment-portfolio-management-tools (noise exemplar — recorded as a negative result)
