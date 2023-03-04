from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.exceptions import FacebookError
import requests

from requests.structures import CaseInsensitiveDict

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
my_account = AdAccount(ACCOUNT_ID)

params = {
  'effective_status': ['ACTIVE', 'PAUSED'],
}

# campaigns = my_account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status]).summary()
"""
ad_creatives = my_account.get_ad_creatives(fields=[Campaign.Field.name, Campaign.Field.start_time,
                                                   Campaign.Field.status, Campaign.Field.status,
                                                   Campaign.Field.start_time], filter=[])
for ad in ad_creatives:
    print(ad)

"""

creative_id = '120330000113530309'
url = f'https://graph.facebook.com/v16.0/{creative_id}/previews?ad_format=DESKTOP_FEED_STANDARD'
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
json_format = requests.get(url, headers=headers).json()
data = json_format["data"]

print("*****")
print(data)
print("*****")

creative = AdCreative('120330000113530309')
creative.remote_read(
    fields=[AdCreative.Field.name, AdCreative.Field.object_story_id]
)

print(creative)

# iterate the whole ad


creative_ad_id = creative['id']
params = {
  'ad_format': AdPreview.AdFormat.mobile_banner
}
try:
  insight = AdCreative(creative_ad_id).get_previews(params=params)

except FacebookError as e:
    print(e)
print({creative_ad_id: insight[0]['body']})

# adsets.load_next_page()
# for adset in adsets:
#    print(adset)
