<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">

        <form action="${request.route_url('checkout')}" method="post">
	        <fieldset class="checkout">
                <legend>Contact Info</legend>
                <table>
              <p> Email:  ${form.email()} </p> </p>
               <p> :${form.phone()} </p>
		</table>
	</fieldset>

	<fieldset class="checkout">
		<legend>Billing Info</legend>
		<table>
		<p> :${form.billing_name()} </p>
		<p> :${form.billing_address_1()} </p>
		<p> :${form.billing_address_2()} </p>
		<p> :${form.billing_city()} </p>
		<p> :${form.billing_state()} </p>
		<p> :${form.billing_zip()} </p>
		<p> :${form.billing_country()} </p>
		</table>
	</fieldset>
		<fieldset class="checkout">
		<legend>Shipping Info</legend>
		<table>
		<p> :${form.shipping_name()} </p>
		<p> :${form.shipping_address_1()} </p>
		<p> :${form.shipping_address_2()} </p>
		<p> :${form.shipping_city()} </p>
		<p> :${form.shipping_state()} </p>
		<p> :${form.shipping_zip()} </p>
		<p> :${form.shipping_country()} </p>
		</table>
	</fieldset>

	<fieldset class="checkout">
		<legend>Credit Card Info</legend>
		<table>
		<p> Credit Card Number: ${form.credit_card_number()} </p>
		<p> Credit Card Type ${form.credit_card_type()} </p>
		<p> Credit Card Expiration Month :${form.credit_card_expire_month()} Year :${form.credit_card_expire_year()} </p>
		<p> CCV: ${form.credit_card_cvv()} </p>
		</table>
	</fieldset>
	<table>
	<tr>
		<th colspan="2">
			<input type="submit" value="Place Order" class="submit" />
		</th>
	</tr>
	</table>
</form>




    </div>
</div>