𝗜𝗱𝗲𝗮 𝗕𝗲𝗵𝗶𝗻𝗱 𝘁𝗵𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁  
Have you ever scrolled through a website full of smartphones and thought: “𝘞𝘩𝘢𝘵 𝘪𝘧 𝘐 𝘤𝘰𝘶𝘭𝘥 𝘤𝘰𝘭𝘭𝘦𝘤𝘵 𝘢𝘭𝘭 𝘵𝘩𝘪𝘴 𝘥𝘢𝘵𝘢 𝘢𝘯𝘥 𝘢𝘯𝘢𝘭𝘺𝘻𝘦 𝘵𝘩𝘦 𝘵𝘳𝘦𝘯𝘥𝘴?”  
That curiosity drove me to start this project, turning raw smartphone listings into a clean dataset and extracting insights that could guide smarter decisions.  

---

𝗪𝗵𝗮𝘁 𝗜 𝗗𝗶𝗱  
1. **𝗪𝗲𝗯 𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴**  
- Used **𝗦𝗲𝗹𝗲𝗻𝗶𝘂𝗺** to scrape live smartphone listings from Smartprix.  
- Automated clicks & scrolling to capture all available products.  
- Stored the entire page source and parsed it with **𝗕𝗲𝗮𝘂𝘁𝗶𝗳𝘂𝗹𝗦𝗼𝘂𝗽**.  

2. **𝗗𝗮𝘁𝗮 𝗖𝗹𝗲𝗮𝗻𝗶𝗻𝗴 & 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗶𝗻𝗴**  
- Extracted 10+ smartphone attributes: model, price, rating, SIM type, processor, RAM, battery, display, camera, card slot, OS.  
- Converted messy text (like “₹14,999”) into numeric form.  
- Handled missing values and inconsistencies.  
- Organized everything into a **𝗣𝗮𝗻𝗱𝗮𝘀 𝗗𝗮𝘁𝗮𝗙𝗿𝗮𝗺𝗲** for analysis.  

3. **𝗘𝘅𝗽𝗹𝗼𝗿𝗮𝘁𝗼𝗿𝘆 𝗗𝗮𝘁𝗮 𝗔𝗻𝗮𝗹𝘆𝘀𝗶𝘀 (𝗘𝗗𝗔)**  
- Explored how **𝗥𝗔𝗠, 𝗯𝗮𝘁𝘁𝗲𝗿𝘆, and 𝗰𝗮𝗺𝗲𝗿𝗮** vary across price ranges.  
- Checked which features **𝗱𝗿𝗶𝘃𝗲 𝘂𝗽 𝘀𝗺𝗮𝗿𝘁𝗽𝗵𝗼𝗻𝗲 𝗽𝗿𝗶𝗰𝗲𝘀**.  
- Identified the **best 𝘀𝗽𝗲𝗰-𝘁𝗼-𝗽𝗿𝗶𝗰𝗲 𝗿𝗮𝘁𝗶𝗼 𝘀𝗺𝗮𝗿𝘁𝗽𝗵𝗼𝗻𝗲𝘀**.  
- Visualized trends in budget vs. flagship devices.  

---

𝗧𝗶𝗹𝗹 𝘄𝗵𝗲𝗿𝗲 𝗜 𝗿𝗲𝗮𝗰𝗵𝗲𝗱  
- Built a **𝗿𝗼𝗯𝘂𝘀𝘁 𝘀𝗰𝗿𝗮𝗽𝗶𝗻𝗴 𝗽𝗶𝗽𝗲𝗹𝗶𝗻𝗲** capable of fetching hundreds of smartphone entries.  
- Created a **𝗰𝗹𝗲𝗮𝗻 𝗱𝗮𝘁𝗮𝘀𝗲𝘁** ready for analysis or modeling.  
- Generated **𝗘𝗗𝗔 𝗶𝗻𝘀𝗶𝗴𝗵𝘁𝘀**:  
  1. Price vs. RAM 📈  
  2. Camera trends across categories 📷  
  3. Battery capacity variations 🔋  

---

𝗙𝘂𝘁𝘂𝗿𝗲 𝗜𝗺𝗽𝗿𝗼𝘃𝗲𝗺𝗲𝗻𝘁𝘀  
- Develop an **interactive dashboard (Plotly/Dash)** for real-time analysis.  
- Automate **periodic scraping** to track smartphone trends over time.  
- Apply **Machine Learning models** to predict smartphone price based on specs.  

---

📂 Shared the dataset + notebooks on GitHub for reproducibility:  
- **𝗪𝗲𝗯 𝗦𝗰𝗿𝗮𝗽𝗶𝗻𝗴**: [GitHub Link](https://github.com/Abhavya-Singh02/Web_Scraping)  
- **𝗗𝗮𝘁𝗮 𝗖𝗹𝗲𝗮𝗻𝗶𝗻𝗴**: [GitHub Link](https://github.com/Abhavya-Singh02/Data-Cleanining-Smart-Phones/tree/main)  
- **𝗘𝗗𝗔**: [GitHub Link](https://github.com/Abhavya-Singh02/Data-Cleanining-Smart-Phones/blob/main/eda_on_smartphone_data.ipynb)  
