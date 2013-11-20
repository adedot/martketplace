__author__ = 'owner'

from marketplace.forms import *
from wtforms import Form, SelectField, TextField, DateTimeField, ValidationError
from wtforms.validators import Email
from marketplace.utils.checkout import *


CARD_TYPES = (('Mastercard','Mastercard'),
             ('VISA','VISA'),
             ('AMEX','AMEX'),
             ('Discover','Discover'),)
def strip_non_numbers(data):
    """ gets rid of all non-number characters """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)


class CheckoutForm(Form):
    email = TextField("email", validators=[Email()])
    phone = TextField("phone")

    #Billing Information
    billing_name = TextField("billing_name", [Required()])
    billing_address_1 = TextField("billing_address_1", [Required()])
    billing_address_2 = TextField("billing_address_2", [Required()])
    billing_city = TextField("billing_city", [Required()])
    billing_state = TextField("billing_state", [Required()])
    billing_zip = TextField("billing_zip", [Required()])
    billing_country = TextField("billing_country", [Required()])

    #Shipping Information

    shipping_name = TextField("shipping_name")
    shipping_address_1 = TextField("shipping_address_1")
    shipping_address_2 = TextField("shipping_address_2")
    shipping_city = TextField("shipping_city")
    shipping_state = TextField("shipping_state")
    shipping_zip = TextField("shipping_zip")
    shipping_country = TextField("shipping_country")
    # Credit Card Information
    credit_card_type = SelectField("credit_card_type", choices=CARD_TYPES)
    credit_card_number = TextField("credit_card_number")
    credit_card_expire_month = DateTimeField("credit_card_expire_month", format="%M")
    #SelectField("credit_card_expire_month",choices=cc_expire_months(), coerce=datetime.datetime)
    credit_card_expire_year =  DateTimeField("credit_card_expire_month", format="%Y")
    #SelectField("credit_card_expire_year",choices=cc_expire_years(), coerce=datetime.datetime)
    credit_card_cvv = TextField("credit_card_cvv")


    def clean_credit_card_number(self):
        """ validate credit card number if valid per Luhn algorithm """
        cc_number = self.cleaned_data['credit_card_number']
        stripped_cc_number = strip_non_numbers(cc_number)
        if not cardLuhnChecksumIsValid(stripped_cc_number):
            raise ValidationError('The credit card you entered is invalid.')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise ValidationError('Enter a valid phone number with area code.(e.g. 555-555-5555)')
        return self.cleaned_data['phone']

