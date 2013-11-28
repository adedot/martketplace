<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>





<!-- Featured Items-->
<div class="hero-unit">

        <form class="form-inline" role="form" action="${request.route_url('product_action',action='search')}" method="post" name="search">
            <div class="form-group">
				<input type="query" class="form-control" id="search" placeholder="Search food, drugs, vitamins">
			  </div>


			  <button type="submit" class="btn btn-default">Search</button>
        </form>

        <br />
        <h1>Get your food, drugs, and vitamins using Okada</h1>

        <br />

    <a href="#" class="btn btn-large btn-success">Learn More here</a>
</div>


