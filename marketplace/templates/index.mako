<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>





<!-- Featured Items-->
<div class="hero-unit">

        <form class="form-inline" role="form" action="${request.route_url('product_action',action='search')}" method="GET" name="search">
            <div class="form-group">
				<input type="query" class="form-control" id="query" name="query" placeholder="Search wine, cakes, electronics">
			  </div>


			  <button type="submit" class="btn btn-default">Search</button>
        </form>

        <br />
        <h1>Get your food at Allen Ikeja Marketplace</h1>

        <br />

    <a href="#" class="btn btn-large btn-success">Learn More here</a>
</div>


