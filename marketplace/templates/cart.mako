<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">
<table summary="Your Shopping Cart" id="shopping_cart">
		<caption>Your Shopping Cart</caption>
		<thead>
			<tr>
				<th scope="col">Product</th>
				<th scope="col">Price</th>
				<th></th>
				<th></th>
				<th></th>
				<th scope="col" class="right">Total</th>
			</tr>
		</thead>
		<tfoot>
			<tr>
				<th class="right" colspan="5">
					Cart Subtotal:
				</th>
				<th class="right">
                    ${cart_subtotal}
				</th>
			</tr>
			% if cart_items:
			<tr>
				<th class="right" colspan="6">
					<form method="GET" action="${request.route_url('checkout')}">
    					<input type="hidden" name="submit" value="Checkout" />

              
              		<input type="submit" value="Checkout" alt="Checkout" />
    				</form>
				</th>
			</tr>
			% endif
		</tfoot>
		<tbody>
		% if cart_items:
			% for item in cart_items:
				<tr>
					<td>
						<a href="${request.route_url('product', id=item.product.id, slug=item.product.slug)}" class="cart">
							${ item.product.name }
						</a>
					</td>
					<td>${ item.product.price }</td>
					<td class="right">
						<form method="post" action="${request.route_url('cart')}">
							<label for="quantity">Quantity:</label>
							<input type="text" name="quantity" value="${ item.quantity }" id="quantity" size="2" class="quantity" maxlength="5" />
							<input type="hidden" name="item_id" value="${ item.product.id }" />
					</td>
					<td>
						<input type="submit" name="submit" value="Update" />
						</form>
					</td>
					<td>
						<form method="post" action="${request.route_url('cart')}" class="cart">
						    <br />
							<input type="hidden" name="item_id" value="${ item.product.id }" />
							<input type="submit" name="submit" value="Remove"/>
						</form>
					</td>
					<td class="right">${ item.total }</td>
				</tr>
			% endfor 
		% else:
		      <tr>
					<td colspan="6" style="height:30px;">
						Your cart is empty.
					</td>
				</tr>
		% endif 
		</tbody>


	</table>

   </div>

</div>