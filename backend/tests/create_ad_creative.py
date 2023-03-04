from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adimage import AdImage, AdImageMixin
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adcreative import AdCreative

import base64
from app.config import APP_ID, APP_SECRET, ACCOUNT_ID, ACCESS_TOKEN, PAGE_ID

FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN, debug=False)
my_account = AdAccount(ACCOUNT_ID)


image = AdImage()
payload = base64.b64encode(open('./../images/gucci-bag.jpg', 'rb').read())

payload = payload.decode('utf-8')

# return same hash_code for same image -
uploaded_image = image.api_create(parent_id=ACCOUNT_ID, params={'bytes': payload})

print(f"{uploaded_image['hash']}  - {uploaded_image['url']}")
# return_val["url"]
# return_val["hash"]

"""<AdImage> {
    "hash": "4f9914935a345227409b2cc7f811928c",
    "height": 1200,
    "name": "bytes",
    "url": "https://scontent-ist1-1.xx.fbcdn.net/v/t45.1600-4/269780490_120330000091595109_3551065005542236_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=2aac32&_nc_ohc=BCQ97sQ9RmoAX9KOoVC&_nc_ht=scontent-ist1-1.xx&edm=AJNyvH4EAAAA&oh=00_AfB2zgiXwEe4msfyOOEfc6CLxqF8RcWyg4PmbUUWGKn1Ng&oe=6403F750",
    "url_128": "https://scontent-ist1-1.xx.fbcdn.net/v/t45.1600-4/269780490_120330000091595109_3551065005542236_n.jpg?stp=dst-jpg_s168x128&_nc_cat=100&ccb=1-7&_nc_sid=cd8e7d&_nc_ohc=BCQ97sQ9RmoAX9KOoVC&_nc_ht=scontent-ist1-1.xx&edm=AJNyvH4EAAAA&oh=00_AfDNdtKwoabuJ1DI968gTquwZmqAylwj_PP0jDhtJ9vFwQ&oe=6403F750",
    "url_256": "https://scontent-ist1-1.xx.fbcdn.net/v/t45.1600-4/269780490_120330000091595109_3551065005542236_n.jpg?stp=dst-jpg_s261x260&_nc_cat=100&ccb=1-7&_nc_sid=cd8e7d&_nc_ohc=BCQ97sQ9RmoAX9KOoVC&_nc_ht=scontent-ist1-1.xx&edm=AJNyvH4EAAAA&oh=00_AfC2Ybht_AxcTMAGkwR7RxyTNQ9oxOOKnSp3QxbufgUfNw&oe=6403F750",
    "url_256_height": "260",
    "url_256_width": "260",
    "width": 1200
}"""

"""
○ The creative link message will be “try it out”
○ The creative link will be “https://www.ounass.ae/designers/gucci”
○ The page id will be “104413048775500”
○ The creative name will be “Gucci AdCreative for Link Ad.”
○ The creative image will be https://ibb.co/pP9hNwV
"""


fields = [AdCreative.Field.id, AdCreative.Field.name, AdCreative.Field.object_story_spec, AdCreative.Field.object_story_id]
params = {
    AdCreative.Field.name: 'Gucci AdCreative for Link Ad.',
    AdCreative.Field.object_story_spec: {
        'page_id': PAGE_ID,

        'link_data': {
            'image_hash': uploaded_image['hash'],
            'link': 'https://www.ounass.ae/designers/gucci',
            'message': 'try it out'
        }
    },

}


"""
<AdCreative> {
    "id": "120330000113543009",
    "name": "Gucci AdCreative for Link Ad. 2023-03-01-c5123e7c619c07b534207c5a501a8419",
    "object_story_spec": {
        "link_data": {
            "image_hash": "4f9914935a345227409b2cc7f811928c",
            "link": "https://www.ounass.ae/designers/gucci",
            "message": "try it out"
        },
        "page_id": "104413048775500"
    }
}


"""



"""
from facebook_business.adobjects.adcreativeobjectstoryspec import AdCreativeObjectStorySpec
from facebook_business.adobjects.adcreativelinkdata import AdCreativeLinkData

link_data = AdCreativeLinkData()
link_data[AdCreativeLinkData.Field.message] = 'try it out'
link_data[AdCreativeLinkData.Field.link] = 'https://www.ounass.ae/designers/gucci”'
link_data[AdCreativeLinkData.Field.image_hash] = uploaded_image['hash']

object_story_spec = AdCreativeObjectStorySpec()
object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = PAGE_ID
object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data

creative = AdCreative(parent_id=ACCOUNT_ID)
creative[AdCreative.Field.name] = 'Gucci AdCreative for Link Ad.'
creative[AdCreative.Field.object_story_spec] = object_story_spec
creative.remote_create()

"""
ad = AdAccount(ACCOUNT_ID).create_ad_creative(fields=fields, params=params)

print(ad)
# Output image Hash
