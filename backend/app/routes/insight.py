from fastapi import Depends, status, APIRouter, Response
from app.database import get_db_session
from sqlalchemy.orm import Session
from app import models

from app.config import ACCESS_TOKEN
import requests
from app import mock_data
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
router = APIRouter()


@router.get('/')
async def insights(ad_set_id: str, db: Session = Depends(get_db_session)):
    # get insights directly from Facebook - results might be too long think about pagination !!!
    # interested about impression and clicks
    url = f'https://graph.facebook.com/v16.0/{ad_set_id}/insights?fields=impressions,clicks'
    json_format = requests.get(url, headers=headers).json()
    data = json_format["data"]
    response = data[0]["body"] if len(data) > 0 else mock_data.insights
    return {'status': 'success', 'insights': response, 'mock_data': len(data) == 0}

