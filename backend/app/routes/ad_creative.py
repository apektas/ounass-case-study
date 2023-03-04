import logging
from typing import Any, Optional, List
from fastapi import Depends, APIRouter
from app.database import get_db_session
from sqlalchemy.orm import Session
from app.models import AdCreativeModel
from fastapi import status, HTTPException
from facebook_business.adobjects.adaccount import AdAccount
from app import crud


from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
router = APIRouter()

fields = ['id', 'name', 'object_story_spec']


@router.post('/', response_model=AdCreativeModel)
async def create_ad_creative(ad_creative_model: AdCreativeModel, db: Session = Depends(get_db_session)) -> Any:
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=False)
    ad_creative_model = AdAccount(ACCOUNT_ID).create_ad_creative(fields=fields, params=ad_creative_model.dict(exclude={'id'}))
    ad_creative_model = AdCreativeModel.parse_obj(ad_creative_model)
    ad_set = crud.create_ad_creative(db, ad_creative_model)
    return AdCreativeModel.from_orm(ad_set)


@router.get('/{ad_creative_id}', response_model=AdCreativeModel)
async def get_ad_set(ad_creative_id: str, db: Session = Depends(get_db_session)) -> Any:

    ad_creative = crud.get_ad_creative_by_id(db, ad_creative_id)
    if ad_creative is None:
        logging.warning(f"Campaign[{ad_creative_id}] not found")
        raise HTTPException(status_code=404,
                            detail={'status_code': 404, 'error_message': f"AdCreative[{ad_creative_id}] not found"})

    return AdCreativeModel.from_orm(ad_creative)


@router.get('/', response_model=List[AdCreativeModel])
async def get_ad_sets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)) -> Any:
    limit = min(100, limit)
    ad_creatives = crud.get_ad_creatives(db, skip, limit)
    return [AdCreativeModel.from_orm(cam) for cam in ad_creatives]



