# Vendor Performance Analysis
I can't upload dataset because they are more than 1.5GB size, so if you want to know then click here: (https://drive.google.com/drive/folders/1zEvsAn6QaK_h_S17vVyCubVzTiT_19VF?usp=sharing)

## 1. Business Problem Statements
Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies need to ensure that they are not incurring losses due to inefficient pricing, poor inventory turnover, or vendor dependency.<br>
### The goal of this analysis is to:
• Identify underperforming brands that require promotional or pricing adjustments.<br>
• Determine top vendors contributing to sales and gross profit.<br>
• Analyze the impact of bulk purchasing on unit costs.<br>
• Assess inventory turnover to reduce holding costs and improve efficiency.<br>
• Investigate the profitability variance between high-performing and low-performing vendors.<br>

## 2. Description
Analyze vendor and brand (Products) performance using sales, purchase, profit, and inventory data to identify top and low-performing vendors, assess inventory turnover, evaluate bulk purchasing impact on costs, and provide insights to optimize profitability, pricing, and supplier dependency.

## 3. Goal of this dashboard
• Identify top-performing and underperforming vendors and brands based on sales, profit, and profit margin.<br>
• Analyze vendor contribution to total sales and purchases to understand dependency risk on specific suppliers.<br>
• Evaluate the impact of bulk purchasing on unit cost reduction and overall profitability.<br>
• Assess inventory turnover to identify slow-moving or unsold stock and reduce holding costs.<br>
• Detect loss-making or low-profit transactions caused by inefficient pricing or heavy discounts.<br>
• Compare profitability between high-selling and low-selling vendors to uncover pricing or volume inefficiencies.<br>
• Understand cost vs revenue behavior across vendors to optimize procurement decisions.<br>
• Support pricing, procurement, and vendor negotiation strategies with data-driven insights.<br>
• Improve cash flow efficiency by reducing capital locked in unsold inventory.<br>
• Enable management to make strategic decisions on vendor diversification, promotions, and supply chain optimization.

## 4.	Tech Stack
### The dashboard was built using the following tools and technologies:<br>
•	📝 Excel – Data is present in ".csv" file.<br>
•	🛢 SQLite3 – For uploading and fetching all the required and summary data to database.<br>
•	👨🏻‍💻 Python – For data modelling and exploratory data analysis (EDA).<br>
•	📊 Power BI Desktop – Main data visualization platform used for report creation.<br>
•	📂 Power Query – Data transformation and cleaning layer for reshaping and preparing the data.<br>
•	🧠 DAX (Data Analysis Expressions) – Used for calculated measures, dynamic visuals, and conditional logic.<br>
•	📁 File Format – .pbix for development and .png for dashboard previews.

## 5. The key visuals
The Vendor Performance Dashboard provides a high-level overview of financial and vendor efficiency metrics in a clean, executive-friendly layout. The top KPI cards highlight total sales of $441.41M, total purchases of $307.34M, gross profit of $134.07M, a healthy 38.7% profit margin, and $2.71M in unsold capital, giving immediate insight into overall business health. A donut chart shows that the top 10 vendors contribute 65.7% of total purchases, emphasizing strong vendor concentration and reliance on key suppliers.<br>
The dashboard further breaks down performance through comparative visuals. Bar charts identify top vendors and top brands by sales, with Diageo North America and brands like Jack Daniel’s and Tito’s leading revenue generation. A dedicated section highlights low-performing vendors and brands, helping decision-makers quickly spot underperformers. The scatter plot mapping total sales against average profit margin clearly distinguishes weaker brands from stronger ones, supporting strategic actions such as vendor optimization, renegotiation, or brand-level performance improvements. Overall, the dashboard effectively combines profitability, vendor contribution, and risk identification into a single analytical view.

## 6. Insights and Business Impact
### Q.1. Identify underperforming brands that require promotional or pricing adjustments?
198 brands exhibit lower sales but higher profit margins, which could benefit from targeted marketing, promotions, or price optimizations to increase volume without compromising profitability.<br>
(https://github.com/Prajin-Kamble/Vendor-Performance-Analysis/blob/main/Analysis%20Screenshot/Brands%20for%20promotional%20and%20pricing%20adjustments.PNG)

### Q.2. Determine top vendors contributing to sales and gross profit?
The top 10 vendors contribute 65.69% of total purchases, while the remaining vendors contribute only 34.31%. This over-reliance on a few vendors may introduce risks such as supply chain disruptions, indicating a need for diversification.<br>
(https://github.com/Prajin-Kamble/Vendor-Performance-Analysis/blob/main/Analysis%20Screenshot/Top%20vendors%20who%20contribution%20is%20high.PNG)

### Q.3. Analyze the impact of bulk purchasing on unit costs?
Vendors buying in large quantities receive a 72% lower unit cost ($10.78 per unit vs. higher unit costs in smaller orders).<br>
Bulk pricing strategies encourage larger orders, increasing total sales while maintaining profitability.<br>
(https://github.com/Prajin-Kamble/Vendor-Performance-Analysis/blob/main/Analysis%20Screenshot/Bulk%20purchasing%20on%20cost.PNG)

### Q.4. Assess inventory turnover to reduce holding costs and improve efficiency?
Total Unsold Inventory Capital: $2.71M<br>
Slow-moving inventory increases storage costs, reduces cash flow efficiency, and affects overall profitability.<br>
Identifying vendors with low inventory turnover enables better stock management, minimizing financial strain.<br>

### Q.5. Investigate the profitability variance between high-performing and low-performing vendors?
1. Top Vendors' Profit Margin (95% CI): (30.74%, 31.61%), Mean: 31.17%<br>
2. Low Vendors' Profit Margin (95% CI): (40.48%, 42.62%), Mean: 41.55%<br>
Low-performing vendors maintain higher margins but struggle with sales volumes, indicating potential pricing inefficiencies or market reach issues.

##### Actionable Insights:
1. Top-performing vendors: Optimize profitability by adjusting pricing, reducing operational costs, or offering bundled promotions.<br>
2. Low-performing vendors: Improve marketing efforts, optimize pricing strategies, and enhance distribution networks.

## 7. Final Recommendations
1. Re-evaluate pricing for low-sales, high-margin brands to boost sales volume without sacrificing profitability.<br>
2. Diversify vendor partnerships to reduce dependency on a few suppliers and mitigate supply chain risks.<br>
3. Leverage bulk purchasing advantages to maintain competitive pricing while optimizing inventory management.<br>
4. Optimize slow-moving inventory by adjusting purchase quantities, launching clearance sales, or revising storage strategies.<br>
5. Enhance marketing and distribution strategies for low-performing vendors to drive higher sales volumes without compromising profit margins.<br>
6. By implementing these recommendations, the company can achieve sustainable profitability, mitigate risks, and enhance overall operational efficiency.

## 8.	Screenshots / Demos
Show what the dashboard looks like. - ![Alt text](https://github.com/username/repo/assets/image.png)
Example: ![Dashboard Preview](https://github.com/Prajin-Kamble/Vendor-Performance-Analysis/blob/main/Snapshot%20of%20dashboard.png)
