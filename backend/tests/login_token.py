from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

my_app_id = '438080767979521'
my_app_secret = 'ff2002ad9af7137b75aafe9e828571e8'
my_access_token = 'EAAGObqCO8AEBAE5lvZBCcwGoZC5v3Ng7wqkkkDqxaOJdLJmk0fw5ZCsZBDZADne8hGlgfeZAE7QMaJNKFpeNk7ZBPeNFxExtDVTagPwQzpYqP9GpFl9xAzwXRlRppT9ZAKp939IwBpLFerJfdb01qiiwZBjOzaVhVhq0uD3BV9tQJvTnvjZBKyWcYCRmlDmA72WbYZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, debug=True)
my_account = AdAccount('act_3061829570753376')
fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status]
campaign = Campaign(120330000091598609).api_get(fields)
# campaigns = my_account.get_campaigns(fields=[Campaign.Field.name, Campaign.Field.start_time, Campaign.Field.status]).summary()
# campaigns = my_account.get_campaigns(fields)
print(campaign)