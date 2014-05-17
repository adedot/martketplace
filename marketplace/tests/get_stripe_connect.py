#__author__ = 'owner'
#
#import oauthlib
#import requests_oauthlib
#import stripe
#import dwolla
#
#
## Create stripe keys
#stripe.api_key = "sk_test_AP2VBnLI89bwW8K41ZmYqBHx"
#
#
## Create bank account
#bank_token = stripe.Token.create(
#  bank_account={
#    "country": 'US',
#    "routing_number": '110000000',
#    "account_number": '000123456789'
#  },
#)
#
#recipient = stripe.Recipient.create(
#  name="Adetola Adewodu",
#  type="individual",
#  bank_account=bank_token['id']
#)
#
#transfer = stripe.Transfer.create(
#  amount=50000,
#  currency="usd",
#  recipient=recipient,
#  description="Transfer for test@example.com"
#)
#
#transfer = stripe.Transfer.create(
#  amount=500,
#  currency="usd",
#  recipient="self",
#  description="Transfer for test@example.com"
#)