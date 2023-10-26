from fastapi import HTTPException
from api.helpers import get_json
from api.utils.constants import news_types


async def get_news(news_type: str):
    if (news_type is None ):
        raise HTTPException(status_code=404, detail={
            "message": f"Field news_type is required!"
        })
    if (news_type not in news_types.keys()):
        raise HTTPException(status_code=404, detail={
            "message": f"No such type of news"
        })

    return get_json(path=f"./api/json/news/{news_types.get(news_type)}_news.json")
