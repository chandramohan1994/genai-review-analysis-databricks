# 🚀 GenAI Review Analysis Pipeline (Databricks + Claude AI)

## 📌 Overview
This project demonstrates how to integrate a cloud-based Generative AI model (Claude by Anthropic) with Databricks to analyze product review data and generate structured insights.

---

## 🔧 What I Built
- Loaded product review data into Databricks
- Integrated Claude API using Python
- Designed prompts to extract:
  - Sentiment (Positive / Negative / Neutral)
  - Summary of reviews
  - Key issues mentioned by users
- Stored AI-generated insights back into a structured table

---

## 🧠 Architecture

Raw Data → Databricks → Claude API → Structured Insights → Databricks Table

---

## ⚙️ Tech Stack
- Databricks (PySpark)
- Python
- Claude API (Anthropic)
- Prompt Engineering

---

## 📊 Example Output

| Review | Sentiment | Summary | Key Issue |
|--------|----------|---------|-----------|
| Good product | Positive | Works well | None |
| Poor battery | Negative | Battery drains fast | Battery issue |

---

## 💡 Key Learnings
- Integration of Generative AI with data pipelines
- Prompt engineering for structured outputs
- Handling unstructured text data
- API integration in Databricks

---

## ⚠️ Note
API keys are not included for security reasons. Add your own Claude API key to run this project.

---

## 🚀 Future Improvements
- Scalable batch processing
- Real-time pipeline integration
- Dashboard visualization (Power BI / Tableau)
