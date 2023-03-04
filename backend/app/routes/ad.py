from fastapi import Depends, status, APIRouter, Response, HTTPException
from app.database import get_db_session
from sqlalchemy.orm import Session
from app import models

from app.config import ACCESS_TOKEN
import requests
from app import mock_data
from requests.structures import CaseInsensitiveDict
from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from app import crud
from typing import List, Any
from app.models import AdModel
import logging


router = APIRouter()


@router.get('/{ad_id}')
async def get_ad(ad_id: str, db: Session = Depends(get_db_session)):
    ad_set = crud.get_ad_by_id(db, ad_id)
    if ad_set is None:
        logging.warning(f"Ad[{ad_id}] not found")
        raise HTTPException(status_code=404,
                            detail={'status_code': 404, 'error_message': f"Ad[{ad_id}] not found"})

    return AdModel.from_orm(ad_set)


@router.post('/')
async def create_ad(ad_model: AdModel, db: Session = Depends(get_db_session)):
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=False)
    fields = ['name', 'id', 'status', 'campaign_id', 'campaign', 'creative', 'status']
    _ad = AdAccount(ACCOUNT_ID).create_ad(fields=fields, params=ad_model.dict(exclude={'id'}))
    # _campaign = Campaign(campaign_model.id).api_get(fields=fields)
    _campaign = AdModel.parse_obj(_ad)
    campaign_db_model = crud.create_ad(db, _campaign)
    return AdModel.from_orm(campaign_db_model)


@router.get('/', response_model=List[AdModel])
async def get_ads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)) -> Any:
    limit = min(100, limit)
    ad_sets = crud.get_ads(db, skip, limit)
    return [AdModel.from_orm(cam) for cam in ad_sets]



