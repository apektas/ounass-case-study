from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi
import requests
from requests.structures import CaseInsensitiveDict
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"


fields = [
]
params = {
  'ad_format':  AdPreview.AdFormat.right_column_standard
}
# a = AdCreative(120330000113530309).get_previews( fields=fields, params=params, )
creative_id = '120330000113643109'
#url = f'https://graph.facebook.com/v16.0/{creative_id}/previews?ad_format=RIGHT_COLUMN_STANDARD'
url = f'https://graph.facebook.com/v16.0/{creative_id}/previews?ad_format=DESKTOP_FEED_STANDARD'
json_format = requests.get(url, headers=headers).json()

print(json_format)



