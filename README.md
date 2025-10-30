# 🌾 Project Samarth – Intelligent Agro-Climate Q&A System

An **AI-powered Q&A prototype** that intelligently answers questions about India's **agriculture and climate data** by connecting datasets from [data.gov.in](https://data.gov.in).  
It allows policymakers, researchers, and citizens to compare rainfall, analyze crop production, and understand the relationship between climate patterns and agriculture.

---

## 🚀 Live Demo
👉 **Try it here:** [Project Samarth on Hugging Face](https://huggingface.co/spaces/kingalan52/Project-Samarth)

*(Hosted permanently using Hugging Face Spaces – powered by Gradio)*

---

## ⚙️ Features
- 🌧️ **Rainfall Comparison:** Compare average rainfall between any two states for a chosen year range (1901–2017)  
- 🌾 **Crop Insights:** View top crops based on latest procurement data (2017–18)  
- 💬 **Interactive Q&A Interface:** Ask data-backed questions with dropdowns for states and years  
- 📊 **Accurate & Traceable:** Each output cites official data sources from IMD and Ministry of Agriculture  

---

## 🧠 System Overview
Project Samarth integrates multiple datasets to enable **cross-domain reasoning** across inconsistent government data formats.  
It uses **Pandas** for real-time data handling and **Gradio** for an intuitive, no-confusion UI.

**Core Workflow:**
1. User selects states and year range  
2. System fetches rainfall data (IMD) and computes averages  
3. It retrieves top crops from procurement data (Ministry of Agriculture)  
4. Results are merged into a single, human-readable report with cited sources  

---

## 🧰 Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, Gradio  
- **Deployment:** Hugging Face Spaces  
- **Data Source:** data.gov.in (IMD & Ministry of Agriculture)

---

## 📘 Datasets Used
1. `Sub_Division_IMD_2017.csv` – Rainfall Data (1901–2017)  
   _Source: India Meteorological Department (IMD), data.gov.in_  
2. `RS_Session_258_AU_1212_2.csv` – Crop Procurement Data (2017–18)  
   _Source: Ministry of Agriculture, data.gov.in_  

---

## 🧩 How to Run Locally
```bash
pip install -r requirements.txt
python app.py
