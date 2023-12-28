import os

from fastapi import FastAPI

from random_skills.ai_service import AIService

kernel = None

app = FastAPI()
ai_service = AIService()

skills_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'skills'))


@app.put("/random-facts")
async def random_country_fact(country: str):

    return {
        "result": ai_service.get_random_fact_about_a_country(country)
    }


@app.put("/jokes")
async def make_a_joke(topic: str):
    return {
        "result": ai_service.make_a_joke(topic)
    }

