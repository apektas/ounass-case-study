from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=True)


fields = [
]
params = {
  'name':  'My Ad [Abdurrahman Pektas]',
  'adset_id': '120330000113546509',
  'creative': {'creative_id': '120330000113543009'},
  'status': 'PAUSED',

}
"""
# finally
INFO:facebook_business.crashreporter:Enabled
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 137' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: fbbizsdk-python-v16.0.0' -d 'name=My+Ad+%5BAbdurrahman+Pektas%5D&adset_id=120330000113546509&creative=%7B%22creative_id%22%3A%22120330000113543009%22%7D&status=PAUSED' 'https://graph.facebook.com/v16.0/act_3061829570753376/ads?access_token=EAAGObqCO8AEBAE5lvZBCcwGoZC5v3Ng7wqkkkDqxaOJdLJmk0fw5ZCsZBDZADne8hGlgfeZAE7QMaJNKFpeNk7ZBPeNFxExtDVTagPwQzpYqP9GpFl9xAzwXRlRppT9ZAKp939IwBpLFerJfdb01qiiwZBjOzaVhVhq0uD3BV9tQJvTnvjZBKyWcYCRmlDmA72WbYZD&appsecret_proof=fc5804a92af26cb0f2a679eaedbdd0c54e67ec8880dd20b16ce8195e1a7b31bc'
<Ad> {
    "id": "120330000113547909"
}

"""
# ad = AdAccount(ACCOUNT_ID).create_ad(fields=fields, params=params)
# print(ad)

## PREVIEW THE ADS
# 'ad_format': AdPreview.AdFormat.facebook_reels_banner_desktop
# 'ad_format': AdPreview.AdFormat.desktop_feed_standard

preview = Ad('120330000113643109').get_previews(params={'ad_format': AdPreview.AdFormat.right_column_standard})
print(preview)
import os
this_dir = os.path.dirname(__file__)
preview_filename = os.path.join(this_dir, 'preview_ad.html')

print("apektas")

preview_file = open(preview_filename, 'w')
preview_file.write(
    "<html><head><title>Facebook Ad Preview</title><body>%s</body></html>"
    % preview[0]["body"]
)
preview_file.close()
