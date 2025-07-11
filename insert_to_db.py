import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_videos(videos):
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cursor = conn.cursor()

        for video in videos:
            cursor.execute("""
                INSERT INTO yt_db.trending (
                    video_id, title, channel, category_id, published_at,
                    tags, view_count, like_count, comment_count
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (video_id) DO NOTHING;
            """, (
                video["video_id"],
                video["title"],
                video["channel"],
                video["category_id"],
                video["published_at"],
                ", ".join(video["tags"]) if isinstance(video["tags"], list) else video["tags"],
                video["view_count"],
                video["like_count"],
                video["comment_count"]
            ))

        conn.commit()
        print(f"✅ Inserted {len(videos)} videos successfully!")

    except Exception as e:
        print("❌ Error inserting videos:", e)

    finally:
        if conn:
            conn.close()
            print("🔌 Connection closed.")