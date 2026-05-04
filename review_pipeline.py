# Databricks notebook source
df = spark.table("workspace.default.amazon")
df.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

api_key = "ENTER YOUR API KEY"

# COMMAND ----------

import anthropic

client = anthropic.Anthropic(api_key="ENTER YOUR API KEY")

message = client.messages.create(
  model="claude-opus-4-7",
  max_tokens=1024,
  messages=[{
    "role": "user",
    "content": "Hello, Claude"
  }]
)
print(message.content[0].text)

# COMMAND ----------

sample_rows = df.limit(10).collect()

summaries = []

for row in sample_rows:
    review_text = row["review_content"]   # ✅ correct column

    response = client.messages.create(
        model="claude-opus-4-7",   # use working model from your test
        max_tokens=150,
        messages=[
            {
                "role": "user",
                "content": f"Summarize this product review:\n{review_text}"
            }
        ]
    )

    summary = response.content[0].text
    summaries.append(summary)

# Convert back to DataFrame
from pyspark.sql import Row

result_data = []
for i in range(len(sample_rows)):
    result_data.append(Row(
        review_content=sample_rows[i]["review_content"],
        summary=summaries[i]
    ))

result_df = spark.createDataFrame(result_data)

display(result_df)

# COMMAND ----------

sample_rows = df.select("review_content").limit(10).collect()

# COMMAND ----------

sentiments = []
summaries = []
key_issues = []

# COMMAND ----------

for row in sample_rows:
    review_text = row["review_content"]

    prompt = f"""
    Analyze this product review and return the answer in exactly this format:

    Sentiment: <Positive/Negative/Neutral>
    Summary: <one-line summary>
    Key Issue: <main issue or None>

    Review:
    {review_text}
    """

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response.content[0].text
    print(response_text)
    print("-----")

# COMMAND ----------

sample_rows = df.select("review_content").limit(10).collect()

sentiments = []
summaries = []
key_issues = []

for row in sample_rows:
    review_text = row["review_content"]

    prompt = f"""
    Analyze this product review and return the answer in exactly this format:

    Sentiment: <Positive/Negative/Neutral>
    Summary: <one-line summary>
    Key Issue: <main issue or None>

    Review:
    {review_text}
    """

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=200,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response.content[0].text

    lines = response_text.split("\n")

    sentiment = ""
    summary = ""
    key_issue = ""

    for line in lines:
        if line.startswith("Sentiment:"):
            sentiment = line.replace("Sentiment:", "").strip()
        elif line.startswith("Summary:"):
            summary = line.replace("Summary:", "").strip()
        elif line.startswith("Key Issue:"):
            key_issue = line.replace("Key Issue:", "").strip()

    sentiments.append(sentiment)
    summaries.append(summary)
    key_issues.append(key_issue)

# COMMAND ----------

from pyspark.sql import Row

result_data = []

for i in range(len(sample_rows)):
    result_data.append(
        Row(
            review_content=sample_rows[i]["review_content"],
            sentiment=sentiments[i],
            summary=summaries[i],
            key_issue=key_issues[i]
        )
    )

result_df = spark.createDataFrame(result_data)

display(result_df)

# COMMAND ----------

