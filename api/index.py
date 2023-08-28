from fastapi import FastAPI, APIRouter

from api.routes import get_schedule_for_date, get_week_schedule

app = FastAPI()
router = APIRouter()

"""
    Parsing website by date
    https://www.kstu.ru/www_Ggrid.jsp?
    with params:
        x=www_GFgrid
        d=(current date)
        f=(facultet id)
        g=(group id)
"""

router.add_api_route(
    path="/week_schedule/{chetnost}",
    endpoint=get_week_schedule
)

router.add_api_route(
    path="/schedule",
    endpoint=get_schedule_for_date,
)


app.router = router
