from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
from datetime import datetime
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
fields = [
  Campaign.Field.name,
  Campaign.Field.id,
  Campaign.Field.status,
  Campaign.Field.start_time,
  Campaign.Field.objective,
  Campaign.Field.special_ad_categories
]
params = {
  'name': 'Conversions Campaign [Abdurrahman Pektas]',
  'objective': 'REACH',
  'status': 'PAUSED',
  'special_ad_categories': [],
  'start_time': datetime.now(),
}

# TODO: check how to delete campaign
campaign = AdAccount(ACCOUNT_ID).create_campaign(
  fields=fields,
  params=params,
)

print(campaign)

