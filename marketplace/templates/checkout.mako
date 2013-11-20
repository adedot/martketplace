<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">

        <form action="." method="post">
	        <fieldset class="checkout">
                <legend>Contact Info</legend>
                <table>
                ${form.email()}
               ${form.phone()}
		</table>
	</fieldset>
	<fieldset class="checkout">
		<legend>Shipping Info</legend>
		<table>
		${form.shipping_name()}
		${form.shipping_address_1()}
		${form.shipping_address_2()}
		${form.shipping_city()}
		${form.shipping_state()}
		${form.shipping_zip()}
		${form.shipping_country()}
		</table>
	</fieldset>
	<fieldset class="checkout">
		<legend>Billing Info</legend>
		<table>
		${form.billing_name()}
		${form.billing_address_1()}
		${form.billing_address_2()}
		${form.billing_city()}
		${form.billing_state()}
		${form.billing_zip()}
		${form.billing_country()}
		</table>
	</fieldset>
	<fieldset class="checkout">
		<legend>Credit Card Info</legend>
		<table>
		${form.credit_card_number()}
		${form.credit_card_type()}
		${form.credit_card_expire_month()}
		${form.credit_card_expire_year()}
		${form.credit_card_cvv()}
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