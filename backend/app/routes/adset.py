import logging
from typing import Any, Optional, List
from fastapi import Depends, status, APIRouter, Response
from app.database import get_db_session
from sqlalchemy.orm import Session
from app import db_models
from facebook_business.adobjects.campaign import Campaign
from app import models
from app import db_models
from app.models import AdSetModel
from fastapi import status, HTTPException
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from app import crud
from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
import random
import string
import app.crud

from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
router = APIRouter()

fields = [
    'id', 'name', 'campaign_id', 'lifetime_budget', 'daily_budget', 'start_time',
    'end_time', 'targeting', 'bid_amount', 'status', 'optimization_goal'
]


@router.post('/', response_model=AdSetModel)
async def create_ad_set(ad_set_model: AdSetModel, db: Session = Depends(get_db_session)) -> Any:
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
    ad_set_model = AdAccount(ACCOUNT_ID).create_ad_set(fields=fields, params=ad_set_model.dict(exclude={'id'}))
    ad_set_model = AdSetModel.parse_obj(ad_set_model)
    ad_set = crud.create_ad_set(db, ad_set_model)
    return AdSetModel.from_orm(ad_set)


@router.get('/{ad_set_id}', response_model=AdSetModel)
async def get_ad_set(ad_set_id: str, db: Session = Depends(get_db_session)) -> Any:

    ad_set = crud.get_ad_set_by_id(db, ad_set_id)
    if ad_set is None:
        logging.warning(f"Campaign[{ad_set_id}] not found")
        raise HTTPException(status_code=404,
                            detail={'status_code': 404, 'error_message': f"AdSet[{ad_set_id}] not found"})

    return AdSetModel.from_orm(ad_set)
    """
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=False)
    _ad_set = AdSet('120330000110071209').api_get(fields=fields)
    _ad_set = AdSetModel.parse_obj(_ad_set)
    # record = crud.get_ad_set_by_id(db, ad_set_id)
    # if record is None:
    #     logging.warning(f"Campaign[{ad_set_id}] not found")
    #     raise HTTPException(
    #         status_code=404,
    #         detail={'status_code': 404, 'error_message': f"Campaign[{ad_set_id}] not found"}
    #     )
    ad_set_db_model = crud.create_ad_set(db, _ad_set)
    return AdSetModel.from_orm(ad_set_db_model)
    """
    #return AdSetModel.from_orm(record)


@router.get('/', response_model=List[AdSetModel])
async def get_ad_sets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)) -> Any:
    limit = min(100, limit)
    ad_sets = crud.get_ad_sets(db, skip, limit)
    return [AdSetModel.from_orm(cam) for cam in ad_sets]



