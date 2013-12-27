<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<div class="span8"> <!--  Content-->
    <div class="input-group">
        <form class="form-inline" role="form" action="${request.route_url('product_action',action='search')}" method="post" name="search">
            <div class="form-group">
				<input type="query" class="form-control" id="search" placeholder="Search food, drugs, vitamins">
			  </div>


			  <button type="submit" class="btn btn-default">Search</button>
        </form>
    </div>
</div> <!-- End of Content -->
<!-- Product Results-->
<div class="span5"> 
    <h1 class="left">Product Results</h1>
    <ul class="nav nav-pills nav-stacked">
     % for product in products:
   <li> <p><b>${product.name}</b> <a href="${request.route_url('product', id=product.id, slug=product.slug)}">
   <img src="${product.image}" height="100" />
   </a></p>
    </li>
    % endfor
    </ul>
</div>

