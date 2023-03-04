from facebook_business.adobjects.page import Page
from facebook_business.api import FacebookAdsApi
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID

FacebookAdsApi.init(access_token=ACCESS_TOKEN, debug=True)
page = Page(PAGE_ID).api_get(fields=[Page.Field.name, Page.Field.id, Page.Field.link])
print(page)