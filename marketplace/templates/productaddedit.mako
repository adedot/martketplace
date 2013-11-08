<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">
        <form action="${request.route_url('product_action',action=action)}" method="post" enctype='multipart/form-data'>
            %if action =='edit':
            ${form.id()}
            %endif

            <p>Name: ${form.name()} </p>
            <p>Brand: ${form.brand()} </p>
            <p>SKU:${form.sku()} </p>
            <p>Price: ${form.price()} </p>
            <p>Active: ${form.is_active()} </p>
            <p>Best Seller: ${form.is_bestseller()} </p>
            <p>Featured: ${form.is_featured()} </p>
            <p>Quantity: ${form.quantity()} </p>
            <p>Description: ${form.description()} </p>
            <p>Key Words: ${form.meta_keywords()} </p>
            <p>Meta Description: ${form.meta_description()} </p>
            <p>Product Picture: ${form.product_picture()} </p>
            <span class="input-group-btn">
                <p><input class="btn btn-default" type="submit" value="Save Product" /></p>
            </span>
        </form>
    </div>
</div>
