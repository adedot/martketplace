<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">
        <form action="${request.route_url('product', id=product.id, slug=product.slug)}" method="post">
        <p>
        <img src="${request.static_url(product.image)}" width="280" height="280" />
        </p>
        <p>Name: <b>${product.name}</b></p>
        <p>Brand: <b>${product.brand}</b></p>
        <p>SKU: <b>${product.sku}</b></p>

        <p>Quantity: <input type="number" name="quantity" value=1 /> </p>

        <p>Price: <b>₦${product.price}</b></p>

        <p> <b>Product Description:</b> </p>
        <p> ${product.description}</p>

        %if product.categories:
        <p> <b> Categories </b></p>
        % for category in product.categories:
             <b> ${category.name} </b>
        % endfor
        % endif

        </p>
         <span class="input-group-btn">
                <p><input class="btn btn-default" type="submit" value="Add to Cart" /></p>
            </span>

        </form>
    </div>

</div>