<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<div class="span5">
	<table id="receipt">
		<caption>Your order has been placed!<br /><br />
			Your Order Number is: ${ order.id }
		</caption>
		<thead>
		<tr>
			<th scope="col">Name</th>
			<th scope="col">Price</th>
			<th scope="col">Quantity</th>
			<th class="right" scope="col">Total</th>
		</tr>
		</thead>
		<tfoot>
			<tr>
				<td colspan="4" class="right" style="height:30px;">
				Order Total: ₦${ order.total}
				</td>
			</tr>
		</tfoot>
		<tbody>
		% for item in order_items:
		<tr>
			<td>${ item.name }</td>
			<td>₦${ item.price}</td>
			<td>${ item.quantity }</td>
			<td class="right">₦${ item.total}</td>
		</tr>
		% endfor
		</tbody>
	</table>
</div>