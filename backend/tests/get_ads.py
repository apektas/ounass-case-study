from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad

my_app_id = '438080767979521'
my_app_secret = 'ff2002ad9af7137b75aafe9e828571e8'
my_access_token = 'EAAGObqCO8AEBAE5lvZBCcwGoZC5v3Ng7wqkkkDqxaOJdLJmk0fw5ZCsZBDZADne8hGlgfeZAE7QMaJNKFpeNk7ZBPeNFxExtDVTagPwQzpYqP9GpFl9xAzwXRlRppT9ZAKp939IwBpLFerJfdb01qiiwZBjOzaVhVhq0uD3BV9tQJvTnvjZBKyWcYCRmlDmA72WbYZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, debug=True)
my_account = AdAccount('act_3061829570753376')

fields = [
  'name',
  'objective',
]
params = {
    'name': 'Conversions Campaign [Abdurrahman Pektas]'
}
filtered = my_account.get_campaigns(fields=fields, params=params)


campaigns = my_account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status], params={'limit': 1000})
for cam in campaigns:
    p = cam.get_insights()
    print(cam, p)


ads = my_account.get_ads(fields=[Ad.Field.id, Ad.Field.name, Ad.Field.id, Ad.Field.adset_id, Ad.Field.status, Ad.Field.preview_shareable_link, Ad.Field.bid_info, Ad.Field.creative], params={'limit': 1000})
for ad in ads:
    print(ad)



# iterate the whole ad sets
adsets = my_account.get_ad_sets(fields=[AdSet.Field.status, AdSet.Field.name, AdSet.Field.campaign, AdSet.Field.created_time], params={'limit': 50})
for ad in adsets:
    print(ad)

params = {
  'effective_status': ['ACTIVE', 'PAUSED'],
}

# campaigns = my_account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status]).summary()
campaigns = my_account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status, ])
for cam in campaigns:
    p = cam.get_insights()
    print(p)
# print(campaigns)

"""



# MOCK ERROR MESSAGE
  Status:  400
  Response:
    {
      "error": {
        "message": "(#80000) There have been too many calls from this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.",
        "type": "OAuthException",
        "code": 80000,
        "error_subcode": 2446079,
        "fbtrace_id": "A3r1FgGq2vRa6IU1aA5kld2"
      }
    }




"""



#adsets.load_next_page()
#for adset in adsets:
#    print(adset)
