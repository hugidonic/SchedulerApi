from fastapi import FastAPI

app = FastAPI()

# https://www.kstu.ru/www_Ggrid.jsp? d=2022-11-09&g=34326

@app.get("/schedule_info")
async def get_schedule_info():
    return {
        "dayOfWeek": "Ср",
        "typeOfWeek": "Нечет",
        "date": "09.11.2022",
    }

@app.get("/subjects")
async def get_schedule_info():
    return [
        None,
        {
            "title": "Основы информационной безопасности",
            "shortTitle": "ОИБ",
            "type": "Лекция",
            "prepod": "Садыков А.М.",
            "cabinet": "И-1-209",
            "date": "1 сен - 1 янв"
        },
        None,
        {
            "title": "Информационные технологии в информационной безопасности",
            "shortTitle": "ИТВИБ",
            "type": "Лабораторная работа",
            "prepod": "Богомолов В.А.",
            "cabinet": "П-7",
            "date": "1 сен - 4 дек"
        },

        {
            "title": "Теория вероятностей и математическая статистика",
            "shortTitle": "ТВИМС",
            "type": "Практика",
            "prepod": "Хайруллин М.Х.",
            "cabinet": "Д-104а",
            "date": "31 окт - 1 янв"
        },
        None,
        None,
        None
    ]

@app.get("/full_schedule")
async def get_schedule_info():
    return {
        "dayOfWeek": "Ср",
        "typeOfWeek": "Нечет",
        "date": "09.11.2022",
        "subjects": [
            None,
            {
                "title": "Основы информационной безопасности",
                "shortTitle": "ОИБ",
                "type": "Лекция",
                "prepod": "Садыков А.М.",
                "cabinet": "И-1-209",
                "date": "1 сен - 1 янв"
            },

            None,
            {
                "title": "Информационные технологии в информационной безопасности",
                "shortTitle": "ИТВИБ",
                "type": "Лабораторная работа",
                "prepod": "Богомолов В.А.",
                "cabinet": "П-7",
                "date": "1 сен - 4 дек"
            },

            {
                "title": "Теория вероятностей и математическая статистика",
                "shortTitle": "ТВИМС",
                "type": "Практика",
                "prepod": "Хайруллин М.Х.",
                "cabinet": "Д-104а",
                "date": "31 окт - 1 янв"
            },
            None,
            None,
            None
        ]
    }