import logging
from functools import lru_cache
from fastapi import FastAPI, Depends, status
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
import uvicorn
from app.config import Settings
from app.routes import ad_creative, campaign, insight, adset, preview, ad
from facebook_business.exceptions import FacebookError, FacebookRequestError
from app import db_models, database
from app import models

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title='Ounass Facebook Marketing Integration',
    description='A pilot project designed to manage Facebook campaign through Facebook marketing API.',
    version='0.0.1',
    contact={
      "name": "Abdurrahman",
    }
)

# origins = [settings.allowed_origins]
origins = ['*']     # allow all for now
logging.error(f"{origins}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(insight.router, tags=['Insights'], prefix='/api/insights')
app.include_router(preview.router, tags=['Preview'], prefix='/api/preview')
app.include_router(campaign.router, tags=['Campaign'], prefix='/api/campaign')
app.include_router(adset.router, tags=['Ad Set'], prefix='/api/adset')
app.include_router(ad_creative.router, tags=['Ad Creative'], prefix='/api/adcreative')
app.include_router(ad.router, tags=['Ad'], prefix='/api/ad')


@app.exception_handler(FacebookError)
async def facebook_request_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.http_status(),
        content={"message": exc.body()},
    )


async def get_settings():
    return Settings()


@app.on_event("startup")
async def startup_event():
    # global instance
    db_models.Base.metadata.create_all(bind=database.engine)


@app.get("/", include_in_schema=False)
async def home():
    response = RedirectResponse(url="/docs")
    return response


@app.get("/info", tags=['Info'])
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        # "items_per_user": settings.items_per_user,
    }

# debugging purpose
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8060)


