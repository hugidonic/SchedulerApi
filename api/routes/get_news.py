from fastapi import HTTPException
from api.helpers import get_json
from api.utils.constants import news_types


async def get_news(news_type: str):
    if (news_type and news_type not in news_types):
        raise HTTPException(status_code=404, detail={
            "message": f"No such type of news"
        })
    return get_json(path=f"./api/json/news/{news_type}_news.json")
