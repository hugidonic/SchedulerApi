from datetime import datetime

from fastapi import HTTPException


def get_date(date: str):
    try:
        return datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        raise HTTPException(status_code=400, detail={
            "message": f"Bad date: {date}"
        })
