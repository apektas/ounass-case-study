from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
import requests
from requests.structures import CaseInsensitiveDict
api = FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)



headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"



ad_set_id = '120330000113024909'
# iterate the whole ad sets
adsets = AdAccount(ACCOUNT_ID).get_ad_sets(fields=[AdSet.Field.id, AdSet.Field.status, AdSet.Field.name, AdSet.Field.campaign, AdSet.Field.created_time], params={'limit': 1000})
count = 1
fields = [
    'impressions',
    'clicks'
]
params = {

}

for ad_set in adsets:
    print(f"Processing [{count}] : {ad_set['id']}")
    # data = AdSet(ad_set['id']).get_insights(fields=fields, params=params)
    url = f'https://graph.facebook.com/v16.0/{ad_set["id"]}/insights?fields=impressions,clicks'
    json_format = requests.get(url, headers=headers).json()
    data = json_format["data"]
    if len(data) > 0:
        print(data[0]["body"])

    count +=1


"""
# mock data
{
  "data": [
    {
      "account_id": "<ACCOUNT_ID>",
      "campaign_id": "<AD_CAMPAIGN_ID>",
      "date_start": "2022-08-29",
      "date_stop": "2022-09-27",
      "impressions": "1000",
      "spend": "100.50",
      "publisher_platform": "instagram",
      "platform_position": "instagram_explore_grid_home"
      'clicks': 'string',
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MAZDZD"
    }
  }
}



"""