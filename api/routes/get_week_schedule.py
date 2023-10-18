from fastapi import HTTPException
import simplejson as json
from api.helpers import get_json
from api.utils import types_of_week


async def get_week_schedule(group: str, chetnost: str):
    with open("./api/json/groups.json", encoding="utf8") as f:
        groups = json.load(f)
        if (group not in groups):
            raise HTTPException(status_code=400, detail={
                "message": f"No such group, try another group. List of available groups: {groups}"
            })


    if chetnost not in types_of_week:
        raise HTTPException(status_code=400, detail={
            "message": "No such type of week, weeks should be only 'chet' or 'nechet'"
        })

    return get_json(path=f"./api/json/{group}/{chetnost}_week.json")