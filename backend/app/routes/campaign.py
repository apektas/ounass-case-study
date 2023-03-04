import logging
from typing import Any, Optional, List
from fastapi import Depends, status, APIRouter, Response, Query
from app.database import get_db_session
from sqlalchemy.orm import Session
from app import db_models
from facebook_business.adobjects.campaign import Campaign
from app import models
from app import db_models
from app.models import CampaignModel
from fastapi import status, HTTPException
from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
import random
import string
from app import crud
router = APIRouter()


@router.post('/', response_model=CampaignModel)
async def create_campaign(campaign_model: CampaignModel, db: Session = Depends(get_db_session)) -> Any:

    if campaign_model.id:
        raise HTTPException(
            status_code=409,
            detail={'status': 409, 'error_message': f"Campaign[{campaign_model.id}] already exists"}
        )

    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=False)
    fields = ['name', 'id', 'status', 'start_time', 'objective', 'special_ad_categories']
    _campaign = AdAccount(ACCOUNT_ID).create_campaign(fields=fields, params=campaign_model.dict(exclude={'id'}))
    # _campaign = Campaign(campaign_model.id).api_get(fields=fields)
    _campaign = CampaignModel.parse_obj(_campaign)
    campaign_db_model = crud.create_campaign(db, _campaign)

    return CampaignModel.from_orm(campaign_db_model)


@router.get('/{campaign_id}', response_model=CampaignModel)
async def get_campaign(campaign_id: str, db: Session = Depends(get_db_session)) -> Any:

    record = crud.get_campaign_by_id(db, campaign_id)
    if record is None:
        logging.warning(f"Campaign[{campaign_id}] not found")
        raise HTTPException(status_code=404,
                            detail={'status_code': 404, 'error_message': f"Campaign[{campaign_id}] not found"})
    return CampaignModel.from_orm(record)


@router.get('/', response_model=List[CampaignModel])
async def get_campaigns(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)) -> Any:
    limit = min(100, limit)
    campaigns = crud.get_campaigns(db, skip, limit)
    return [CampaignModel.from_orm(cam) for cam in campaigns]



