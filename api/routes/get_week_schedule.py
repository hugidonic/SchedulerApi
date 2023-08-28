from fastapi import HTTPException

from api.helpers import get_json
from api.utils import types_of_week


async def get_week_schedule(chetnost: str):
    if chetnost not in types_of_week:
        raise HTTPException(status_code=400, detail={
            "message": "No such type of week"
        })

    return get_json(path=f"./api/json/{chetnost}_week.json")
