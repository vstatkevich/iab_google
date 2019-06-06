import numpy as np
import pandas as pd
from pandas.io.json import json_normalize 
import urllib.request
import json
import tldextract

print('start')

iabVendorListUrl = 'https://vendorlist.consensu.org/vendorlist.json'
googleProvidersUrl = 'https://storage.googleapis.com/adx-rtb-dictionaries/providers.csv'
outputFilePath = 'iab_google_mapping.csv'

def clear_url(origin_url):
  return tldextract.extract(origin_url).registered_domain

# download and prepare IAB vendors
with urllib.request.urlopen(iabVendorListUrl) as response:
  vendorlist = json.loads(response.read().decode())
df_iab = json_normalize(vendorlist['vendors'])
df_iab['policyUrl'] = df_iab['policyUrl'].apply(clear_url)

# download and prepare Google providers
df_google = pd.read_csv(googleProvidersUrl)
df_google['policy_url'] = df_google['policy_url'].apply(clear_url)

# intersect IAB and Google
intersected_df = pd.merge(df_iab, df_google, how='inner', left_on='policyUrl', right_on='policy_url')
clean_df = intersected_df[['id','name','policyUrl','provider_id','provider_name']]

# write result to csv
clean_df.to_csv(outputFilePath, index=False)

print(f'{outputFilePath} is ready')