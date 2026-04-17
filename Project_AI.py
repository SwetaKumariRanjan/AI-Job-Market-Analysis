import pandas as pd

df_jobs = pd.read_csv(r"C:\Users\user\Downloads\archive (2)\DataAnalyst.csv")
df_salary = pd.read_csv(r"C:\Users\user\Downloads\archive\ds_salaries.csv")
df_ai = pd.read_csv(r"C:\Users\user\Downloads\archive (1)\AI Job Market Dataset.csv")

print(df_jobs.head())
print(df_salary.head())
print(df_ai.head())

# For jobs dataset
df_jobs.drop_duplicates(inplace=True)
df_jobs.dropna(inplace=True)

# For salary dataset
df_salary.drop_duplicates(inplace=True)
df_salary.dropna(inplace=True)

# For AI dataset
df_ai.drop_duplicates(inplace=True)
df_ai.dropna(inplace=True)

print(df_jobs.info())
print(df_salary.info())
print(df_ai.info())

df_jobs.columns = df_jobs.columns.str.lower().str.replace(" ", "_")
df_salary.columns = df_salary.columns.str.lower().str.replace(" ", "_")
df_ai.columns = df_ai.columns.str.lower().str.replace(" ", "_")

df_salary["salary_in_usd"] = pd.to_numeric(df_salary["salary_in_usd"], errors='coerce')

df_jobs.fillna("Unknown", inplace=True)
df_ai.fillna("Unknown", inplace=True)

df_jobs["job_title"] = df_jobs["job_title"].str.lower()
df_salary["job_title"] = df_salary["job_title"].str.lower()
df_jobs["location"] = df_jobs["location"].str.lower()

print(df_jobs["job_title"].value_counts().head())
print(df_salary["experience_level"].value_counts())

print(df_jobs.shape)
print(df_salary.shape)
print(df_ai.shape)

df_jobs.to_csv("clean_jobs.csv", index=False)
df_salary.to_csv("clean_salary.csv", index=False)
df_ai.to_csv("clean_ai_jobs.csv", index=False)

#EDA
print(df_jobs.head())
print(df_jobs.shape)
print(df_jobs.columns)

df_jobs["job_title"].value_counts().head(10)

df_jobs["location"].value_counts().head(10)

df_salary.groupby("job_title")["salary_in_usd"].mean().sort_values(ascending=False)

skills = ["python", "sql", "excel", "power bi", "tableau"]
for skill in skills:
    df_jobs[skill] = df_jobs["job_description"].str.lower().apply(lambda x: 1 if skill in x else 0)
df_jobs[skills].sum()


