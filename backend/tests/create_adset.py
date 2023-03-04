from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID
from datetime import datetime, timedelta
FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
fields = [
]
params = {
  'name': 'Conversions Campaign [Abdurrahman Pektas]',
  'objective': 'REACH',
  'status': 'PAUSED',
  'special_ad_categories': [],
}


fields = ['id', 'name', 'campaign_id', 'lifetime_budget', 'daily_budget', 'start_time',
          'end_time', 'targeting', 'bid_amount', 'status', 'optimization_goal']

now = datetime.now()

params = {
    'name': 'My first Adset [Abdurrahman Pektas]',
    'daily_budget': 2000,
    'start_time': now,
    'end_time': now + timedelta(days=10),
    'campaign_id': '120330000091598609',
    'bid_strategy': AdSet.BidStrategy.lowest_cost_with_bid_cap,
    'bid_amount': 100,
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'targeting': {
        'age_min': 20,
        'age_max': 35,
        'geo_locations': {
          'countries': ['AE', 'SA', 'KW']  # the county codes of the UAE, KSA, KUWAIT
        },
        'facebook_positions': ['feed']},
    'status': 'PAUSED',
}

#campaign = AdAccount(ACCOUNT_ID).create_ad_set(fields=fields, params=params)
#print(campaign)

"""
<AdSet> {
    "bid_amount": 5,
    "campaign_id": "120330000091598609",
    "daily_budget": "2000",
    "end_time": "2023-03-12T04:10:14+0400",
    "id": "120330000113541909",
    "lifetime_budget": "0",
    "name": "My first Adset [Abdurrahman Pektas]",
    "optimization_goal": "REACH",
    "start_time": "2023-03-02T04:10:14+0400",
    "status": "PAUSED",
    "targeting": {
        "age_max": 35,
        "age_min": 20,
        "facebook_positions": [
            "feed"
        ],
        "geo_locations": {
            "countries": [
                "SA",
                "AE",
                "KW"
            ],
            "location_types": [
                "home"
            ]
        }
    }
}



120330000113543509 - status active
120330000113544509 - bid -10
120330000113545509 - bid 30
120330000091598609 - bid 100
"""







params = {
  'effective_status': ['ACTIVE', 'PAUSED'],
}

# remote_delete
# AdSet('120330000113536709').api_delete()
# NOTE: set status as deleted once api_delete is executed 120330000113546509
remote_campaign = AdSet('120330000113546509').api_get(fields=fields, params=params)
print(remote_campaign)
