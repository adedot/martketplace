<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<script src="${request.static_url('marketplace:static/js/shipping_fields.js')}"></script>
<!-- Adding Stripe js -->
<script type="text/javascript" src="https://js.stripe.com/v2/"></script>
<script type="text/javascript">
  // This identifies your website in the createToken call below
  Stripe.setPublishableKey('pk_test_xfanUtHUE86panM02JbeJPTw');
  // ...



var stripeResponseHandler = function(status, response) {
  var $form = $('#payment-form');

  if (response.error) {
    // Show the errors on the form
    $form.find('.payment-errors').text(response.error.message);
    $form.find('button').prop('disabled', false);
  } else {
    // token contains id, last4, and card type
    var token = response.id;
    // Insert the token into the form so it gets submitted to the server
    $form.append($('<input type="hidden" name="stripeToken" />').val(token));
    // and submit
    $form.get(0).submit();
  }
};

  jQuery(function($) {
  $('#payment-form').submit(function(event) {
    var $form = $(this);

    // Disable the submit button to prevent repeated clicks
    $form.find('button').prop('disabled', true);

    Stripe.card.createToken($form, stripeResponseHandler);

    // Prevent the form from submitting with the default action
    return false;
  });
});

</script>


<div class="span5"> <!--  Content-->
    <div class="input-group">
        <form action="${request.route_url('checkout')}" method="post" id="payment-form">
	        <fieldset class="checkout">
                <legend>Contact Info</legend>
                <table>
              <p> Email:        ${form.email()} </p>
               <p>Phone:        ${form.phone()} </p>
                </table>
            </fieldset>

            <fieldset class="checkout">
                <legend>Billing Info</legend>
                <table>
                <p> Name:               ${form.billing_name()} </p>
                <p> Address Line #1:    ${form.billing_address_1()} </p>
                <p> Address Line #2 :   ${form.billing_address_2()} </p>
                <p> City:               ${form.billing_city()} </p>
                <p> State:              ${form.billing_state()} </p>
                <p> Zipcode:            ${form.billing_zip()} </p>
                <p> Country:           ${form.billing_country()} </p>
                </table>
            </fieldset>


              <div id="shipping_fields">
              <input type="checkbox" id="same_billing_shipping" defaultChecked="false">Same as billing<br>
                <fieldset class="checkout">
                <legend>Shipping Info</legend>
                <table>
                <p> Name:   ${form.shipping_name()} </p>
                <p> Address Line #1:    ${form.shipping_address_1()} </p>
                <p> Address Line #2:    ${form.shipping_address_2()} </p>
                <p> City:   ${form.shipping_city()} </p>
                <p> State:  ${form.shipping_state()} </p>
                <p> Zipcode:    ${form.shipping_zip()} </p>
                <p> Country:    ${form.shipping_country()} </p>
                </table>
            </fieldset>
            </div>

            <fieldset class="checkout">
                <legend>Credit Card Info</legend>
                <table>
                <span class="payment-errors"></span>

              <div class="form-row">
                <label>
                  <span>Card Number</span>
                  <input type="text" size="20" data-stripe="number"/>
                </label>
              </div>

              <div class="form-row">
                <label>
                  <span>CVC</span>
                  <input type="text" size="4" data-stripe="cvc"/>
                </label>
              </div>

              <div class="form-row">
                <label>
                  <span>Expiration (MM/YY)</span>
                  <input type="text" size="2" data-stripe="exp-month"/>
                </label>
                <span> / </span>
                <input type="text" size="4" data-stripe="exp-year"/>
              </div>

                </table>
            </fieldset>
            <table>
            <tr>
                <th colspan="2">
                    <button type="submit">Submit Payment</button>

                </th>
            </tr>
            </table>
    </form>




    </div>
</div>