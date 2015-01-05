<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<div class="span5">
	<table id="receipt" cellpadding="10" cellspacing="10">
		<caption><h2>Your order has been placed!</h2><br /><br />
			<h3>Your Order Number is: ${ order.id }</h3>
		</caption>
		<thead>
		<tr>
		    <th scope="col">Image</th>
			<th scope="col">Name</th>
			<th scope="col">Price</th>
			<th scope="col">Quantity</th>
			<th class="right" scope="col">Total</th>
		</tr>
		</thead>
		<tfoot>
			<tr>
			    <th class="right" colspan="4">
					Order Total:
				</th>
				<th class="right">

				₦${ order.total}
				</td>
			</tr>
		</tfoot>
		<tbody>
		% for item in order_items:
		<tr>
		    <td>
                <a href="${request.route_url('product', id=item.product.id, slug=item.product.slug)}" class="cart">
                    <img src="${request.static_url(item.product.image)}" width="140" height="140" />
                </a>
            </td>
			<td>${ item.name }</td>
			<td>₦${ item.price}</td>
			<td>${ item.quantity }</td>
			<td class="right">₦${ item.total}</td>
		</tr>
		% endfor
		</tbody>
	</table>
</div>