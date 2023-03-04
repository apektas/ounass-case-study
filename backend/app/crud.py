from sqlalchemy.orm import Session
from app.db_models import AdSet, Campaign, AdCreative, Ad
from app.models import AdSetModel, CampaignModel, AdCreativeModel, AdModel


def get_campaigns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Campaign).offset(skip).limit(limit).all()


def get_ad_sets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AdSet).offset(skip).limit(limit).all()


def get_campaign_by_id(db: Session, campaign_id: str):
    return db.query(Campaign).filter(Campaign.id == campaign_id).first()


def get_ad_set_by_id(db: Session, ad_set_id: str):
    return db.query(AdSet).filter(AdSet.id == ad_set_id).first()


def create_ad_set(db: Session, ad_set: AdSetModel):
    # check ad set
    campaign = get_campaign_by_id(db, ad_set.campaign_id)
    if not campaign:
        raise Exception(f"Campaign[{ad_set.campaign_id}] not found")
    _ad_set = AdSet(**ad_set.dict(exclude={'billing_event', 'ends_after'}))
    db.add(_ad_set)
    db.commit()
    db.refresh(_ad_set)
    return _ad_set


def create_campaign(db: Session, campaign: CampaignModel):
    # check campaign
    campaign_db_model = Campaign(**campaign.dict(exclude={'special_ad_categories'}))
    db.add(campaign_db_model)
    db.commit()
    db.refresh(campaign_db_model)
    return campaign_db_model


# Ad Creative

def create_ad_creative(db: Session, ad_creative: AdCreativeModel):
    # check campaign
    ad_creative_db_model = AdCreative(**ad_creative.dict())
    db.add(ad_creative_db_model)
    db.commit()
    db.refresh(ad_creative_db_model)
    return ad_creative_db_model


def get_ad_creatives(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AdCreative).offset(skip).limit(limit).all()


def get_ad_creative_by_id(db: Session, ad_creative_id: str):
    return db.query(AdCreative).filter(Ad.id == ad_creative_id).first()


# AD CRUD Operations
def create_ad(db: Session, ad: AdModel):
    # check campaign
    ad_db_model = Ad(**ad.dict())
    db.add(ad_db_model)
    db.commit()
    db.refresh(ad_db_model)
    return ad_db_model


def get_ads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ad).offset(skip).limit(limit).all()


def get_ad_by_id(db: Session, ad_id: str):
    return db.query(Ad).filter(Ad.id == ad_id).first()
