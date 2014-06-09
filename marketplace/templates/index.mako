<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>





<!-- Featured Items-->
<div class="hero-unit">


        <br />
        <h1>Search for wine, cakes, and electronics at Allen Ikeja Marketplace</h1>

        <br />
        <form class="form-inline" role="form" action="${request.route_url('product_action',action='search')}" method="GET" name="search">
            <div class="form-group">
				<input type="query" class="form-control" id="query" name="query" placeholder="Search wine, cakes, electronics">
			  </div>


			  <button type="submit" class="btn btn-default">Search</button>
        </form>

        <!-- Add Popular wines, cakes and electronics -->

        <!-- 2 wines, 2 cakes, 2 electronics -->




</div>


