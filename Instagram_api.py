import os
from fastapi import FastAPI, Request, HTTPException, Query
from dotenv import load_dotenv
import instaloader

load_dotenv()

API_PASSWORD = os.getenv("API_PASSWORD")

app = FastAPI()

@app.get("/instagram-post")
async def get_instagram_post_info(
    request: Request,
    shortcode: str = Query(..., description="Короткий код поста в Instagram (например, 'Cxyz1234')")
):
    api_key = request.headers.get("X-API-Key")
    if api_key != API_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized: неправильний ключ")

    try:
        loader = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        return {
            "shortcode": shortcode,
            "author": post.owner_username,
            "caption": post.caption,
            "likes": post.likes,
            "comments": post.comments,
            "posted_at": post.date_utc.isoformat()
        }

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"❌ Пост не знайдено або помилка: {str(e)}")