__author__ = 'owner'

import braintree

from datetime import datetime


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    "cn92b7xdrk4bgzwn",
    "2jzzb8hxjsj4jbgw",
    "4023624c52e3f5413490a53884e449e3"
)

amount = "1000.00"
credit_card_number = "4111111111111111"
expiration_month = "05"
expiration_year = "2012"


#result = braintree.Transaction.sale({
#    "amount": amount,
#    "credit_card": dict(number=credit_card_number, expiration_month=expiration_month, expiration_year=expiration_year)
#})
#
#
#
#
#if result.is_success:
#    print "success!: " + result.transaction.id
#elif result.transaction:
#    print "Error processing transaction:"
#    print "  message: " + result.message
#    print "  code:    " + result.transaction.processor_response_code
#    print "  text:    " + result.transaction.processor_response_text
#else:
#    print "message: " + result.message
#    for error in result.errors.deep_errors:
#        print "attribute: " + error.attribute
#        print "  code: " + error.code
#        print "  message: " + error.message



month_choice = []
# month_choice.append(('','- Month -'))
for i in range(1,13):
    if len(str(i)) == 1:
        numeric = '0' + str(i)
    else:
        numeric = str(i)
    month_choice.append((numeric, datetime(2009, i, 1).strftime('%B')))
MONTHS = tuple(month_choice)


calendar_years = []
# calendar_years.append(('','- Year -'))
for i in range(datetime.now().year, datetime.now().year+10):
    calendar_years.append((i,i))
YEARS = tuple(calendar_years)

def cc_expire_years():
    """ list of years starting with current twelve years into the future """
    current_year = datetime.datetime.now().year
    years = range(current_year, current_year+12)
    return [(str(x),str(x)) for x in years]

def cc_expire_months():
    """ list of tuples containing months of the year for use in credit card form.
    [('01','January'), ('02','February'), ... ]

    """
    months = []
    for month in range(1,13):
        if len(str(month)) == 1:
            numeric = '0' + str(month)
        else:
            numeric = str(month)
        months.append((numeric, datetime.date(2009, month, 1).strftime('%B')))
    return months

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a Luhn mod-10 checksum
    Taken from: http://code.activestate.com/recipes/172845/

    """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(0, num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    return ( (sum % 10) == 0 )