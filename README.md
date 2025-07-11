# 📈 YouTube Trending Insights Tracker

An end-to-end automated ETL pipeline that fetches daily trending videos from YouTube (India), transforms the data, and loads it into a PostgreSQL database hosted on Supabase — all orchestrated using GitHub Actions. Designed for portfolio showcase and to demonstrate practical data engineering skills using beginner-friendly tools and real-world APIs.

---

## 🚀 Features

- ⏰ **Daily Automation** via GitHub Actions (6 AM UTC)
- 🔄 **ETL Pipeline** using Python scripts
- 🌐 **YouTube Data API v3** integration
- 🧹 **Data Cleaning & Transformation** included
- 🛢️ **PostgreSQL Storage** on Supabase
- 📊 Ready for **SQL-based Analysis**
- ✅ **Error Handling** and idempotent inserts

---

## 🛠️ Tech Stack

| Layer        | Tools Used                                      |
|--------------|-------------------------------------------------|
| Extract      | YouTube Data API v3                             |
| Transform    | Python + Pandas                                 |
| Load         | PostgreSQL (via Supabase)                       |
| Automation   | GitHub Actions (cron + manual dispatch)         |
| Deployment   | Hosted entirely on GitHub + Supabase            |

---

## 🔄 How It Works

1. **Extract**: Python script (`get_trending.py`) pulls top 50 trending videos for region `IN` using YouTube API.
2. **Transform**: The script formats and prepares relevant fields (title, channel, tags, view count, etc.).
3. **Load**: Clean data is inserted into a `trending` table in the Supabase PostgreSQL DB.
4. **Automate**: GitHub Actions workflow (`.github/workflows/etl-cron.yml`) runs the job every morning at 6 AM UTC.

---

## 🧪 Sample Output Screenshot

> Here's a snapshot of the `trending` table populated in Supabase:

📸 *(Add your screenshot below)*

<img width="1366" height="563" alt="Screenshot 2025-07-11 152322" src="https://github.com/user-attachments/assets/3fe7eeea-3cfa-493e-9925-4a9fac6b7a0f" />


---

## 📂 Project Structure

```plaintext
├── get_trending.py         # Main ETL script
├── insert_to_db.py         # Database insertion logic
├── main.py                 # DB test connection script
├── requirements.txt        # Python dependencies
├── .github
│   └── workflows
│       └── etl-cron.yml    # GitHub Actions workflow
└── README.md               # Project documentation
