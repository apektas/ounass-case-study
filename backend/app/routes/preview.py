from fastapi import Depends, status, APIRouter, Response
from app.database import get_db_session
from sqlalchemy.orm import Session
from facebook_business.adobjects.adpreview import AdPreview

import os
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID


router = APIRouter()


@router.get('/{ad_id}')
async def preview_ad(ad_id: str, db: Session = Depends(get_db_session)):
    # get insights directly from Facebook - results might be too long think about pagination !!!
    # interested about impression and clicks
    FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
    preview = Ad(ad_id).get_previews(params={'ad_format': AdPreview.AdFormat.desktop_feed_standard})
    this_dir = os.path.dirname(__file__)
    preview_filename = os.path.join(this_dir+'/../../previews/', f'{ad_id}.html')
    preview_file = open(preview_filename, 'w')
    preview_file.write(
        f"<html><head><title>Facebook Ad Preview - Ad-Id {ad_id}</title><body>{preview[0]['body']}</body></html>"
    )
    preview_file.close()

    return {'body': preview[0]["body"]}

