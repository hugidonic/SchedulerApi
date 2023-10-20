from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from api.routes import get_schedule_for_date, get_week_schedule, get_news

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
    path="/week_schedule",
    endpoint=get_week_schedule
)

router.add_api_route(
    path="/schedule",
    endpoint=get_schedule_for_date,
)

router.add_api_route(
    path="/news",
    endpoint=get_news,
)


app.router = router
app.mount("/static", StaticFiles(directory="./static"), name='static')
