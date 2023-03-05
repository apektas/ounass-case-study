from pydantic import BaseModel, Json
from datetime import datetime, timedelta
from typing import Optional, Any, List


class CampaignModel(BaseModel):
    id: Optional[str] = ""
    name: Optional[str] = "Conversions Campaign [Abdurrahman Pektas]"
    objective: Optional[str] = "REACH"
    status: Optional[str] = "PAUSED"
    special_ad_categories = []

    class Config:
        orm_mode = True


class LocationsModel(BaseModel):
    countries: Optional[List[str]] = ['AE', 'SA', 'KW']
    location_types: Optional[List[str]] = ["home"]


class TargetingModel(BaseModel):
    age_min: Optional[int] = 20
    age_max: Optional[int] = 35
    facebook_positions: Optional[List[str]] = ["story"]
    geo_locations: Optional[LocationsModel] = None


class AdSetModel(BaseModel):
    id: str = None
    name: str = 'My first Adset [Abdurrahman Pektas]'
    daily_budget: int = 2000
    bid_amount: int = 5
    daily_budget: int
    ends_after = 10
    start_time: datetime = datetime.now()
    end_time: datetime = datetime.now() + timedelta(days=10)
    targeting: Optional[TargetingModel] = None
    campaign_id: str
    billing_event:  str = 'IMPRESSIONS'
    optimization_goal: str = 'REACH'
    status: str = 'PAUSED'

    class Config:
        orm_mode = True


class LinkDataModel(BaseModel):
    image_hash: str = '4f9914935a345227409b2cc7f811928c'
    link: str = 'https://www.ounass.ae/designers/gucci'
    message: str = 'try it out'


class ObjectStorySpecModel(BaseModel):
    page_id: str = '104413048775500'
    link_data: Optional[LinkDataModel]


class AdCreativeModel(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = 'Gucci AdCreative for Link Ad.'
    object_story_spec: Optional[ObjectStorySpecModel]

    class Config:
        orm_mode = True


class CreativeModel(BaseModel):
    creative_id: Optional[str] = '120330000113543009'


class AdModel(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = 'My Ad [Abdurrahman Pektas]'
    adset_id: Optional[str] = '120330000113645409'
    creative: Optional[CreativeModel]
    status: str = 'PAUSED'

    class Config:
        orm_mode = True


