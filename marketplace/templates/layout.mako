<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      xmlns:tal="http://xml.zope.org/namespaces/tal"
      metal:define-macro="layout" lang="en">
<head>
    <title>${title}</title>

         <link rel="stylesheet"
      href="${request.static_url('marketplace:static/css/bootstrap.css')}"/>
    <link rel="stylesheet"
          href="${request.static_url('marketplace:static/bootstrap/css/bootstrap-responsive.css')}" />

    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/prettyPhoto.css')}">
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/flexslider.css')}">
    
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/font-awesome.css')}">
    
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/sidebar-nav.css')}">
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/style.css')}">
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/black.css')}">
      <!-- JS -->
    <script src="http://code.jquery.com/jquery.js"></script>
    <!-- Bootstrap 3 -->
    <script src="${request.static_url('marketplace:static/js/bootstrap.js')}"></script>
    <!-- Pretty Photo -->
    <script src="${request.static_url('marketplace:static/js/jquery.prettyPhoto.js')}"></script>
    <!-- Filter for support page -->
    <script src="${request.static_url('marketplace:static/js/filter.js')}"></script>
     <!-- Flex slider -->
    <script src="${request.static_url('marketplace:static/js/jquery.flexslider-min.js')}"></script>
    <!-- Carousel for recent posts -->
    <script src="${request.static_url('marketplace:static/js/jquery.carouFredSel-6.1.0-packed.js')}"></script>
    <script src="${request.static_url('marketplace:static/js/custom.js')}"></script> <!-- Custom codes -->
    
    

      <!-- HTML5 Support for IE -->
  <!--[if lt IE 9]>
  <script src="${request.static_url('marketplace:static/js/html5shim.js')}"></script>
  <![endif]-->

  <!-- Favicon -->
  <link rel="shortcut icon" href="${request.static_url('marketplace:static/img/favicon/favicon.png')}">
</head>
<body>

<!-- Header starts -->
  <header>
    <div class="container">
      <div class="row">

        <div class="col-md-4">
          <!-- Logo. Use class "color" to add color to the text. -->
          <div class="logo">
            <h1><a href="${request.route_url('home')}">Okada<span class="color bold">Market Place</span></a></h1>
            <p class="meta">online shopping is fun!!!</p>
          </div>
        </div>

        <div class="col-md-5 col-md-offset-3 pull-right">

          <!-- Search form -->
            <form class="form-inline" role="form" action="${request.route_url('product_action',action='search')}" method="post" name="search">
			  <div class="form-group">
				<input type="query" class="form-control" id="search" placeholder="Search">
			  </div>


			  <button type="submit" class="btn btn-default">Search</button>
			</form>

          <div class="hlinks">
            <span>

              <!-- item details with price -->
              <a href="${request.route_url('cart')}" role="button" data-toggle="modal">3 Item(s) in your <i class="icon-shopping-cart"></i></a> -<span class="bold">$25</span>

            </span>

            <span>

            <!-- Add Checkout -->
            <a href="${request.route_url('checkout')}">Checkout</a>
            </span>


              <!-- Login and Register link -->
              <span class="lr"><a href="#login" role="button" data-toggle="modal">Login</a> or <a href="#register" role="button" data-toggle="modal">Register</a></span>

          </div>

        </div>

      </div>
    </div>
  </header>
  <!-- Header ends -->


   <!-- Navigation -->
          <div class="navbar bs-docs-nav" role="banner">

             <div class="container">
               <div class="navbar-header">
				  <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".bs-navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				  </button>

				</div>
               <nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation">
                 <ul class="nav navbar-nav">
                   <li><a href="${request.route_url('home')}"><i class="icon-home"></i></a></li>
                   <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown">Account <b class="caret"></b></a>
                      <ul class="dropdown-menu">
                        <li><a href="myaccount.html">My Account</a></li>
                        <li><a href="view-cart.html">View Cart</a></li>
                        <li><a href="checkout.html">Checkout</a></li>
                        <li><a href="wish-list.html">Wish List</a></li>
                        <li><a href="order-history.html">Order History</a></li>
                        <li><a href="edit-profile.html">Edit Profile</a></li>
                        <li><a href="confirmation.html">Confirmation</a></li>
                      </ul>
                   </li>
                   <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown">Pages <b class="caret"></b></a>
                      <ul class="dropdown-menu">
                        <li><a href="general.html">General</a></li>
                        <li><a href="login.html">Login</a></li>
                        <li><a href="register.html">Register</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Blog Single</a></li>
                        <li><a href="404.html">404</a></li>
                      </ul>
                   </li>
                   <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown">Ladies <b class="caret"></b></a>
                      <ul class="dropdown-menu">
                        <li><a href="items.html">Bags</a></li>
                        <li><a href="items.html">Shoes</a></li>
                        <li><a href="items.html">Handbags</a></li>
                        <li><a href="items.html">Accessories</a></li>
                        <li><a href="items.html">Cosmetics</a></li>
                      </ul>
                   </li>
                   <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown">Confectionaries <b class="caret"></b></a>
                      <ul class="dropdown-menu">
                        <li><a href="items.html">Cakes</a></li>
                        <li><a href="items.html">Vitamins</a></li>
                        <li><a href="items.html">Drugs</a></li>
                      </ul>
                   </li>
                   <li><a href="support.html">Support</a></li>
                   <li><a href="contact.html">Contact</a></li>
                 </ul>
               </nav>
              </div>
           </div>

<div class="items">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        ${next.body()}
      </div>
   </div>
  </div>
</div>

<!-- Footer starts -->
<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-12">

            <div class="row">

              <div class="col-md-4">
                <div class="widget">
                  <h5>Contact</h5>
                  <hr />
                    <div class="social">
                      <a href="#"><i class="icon-facebook facebook"></i></a>
                      <a href="#"><i class="icon-twitter twitter"></i></a>
                      <a href="#"><i class="icon-linkedin linkedin"></i></a>
                      <a href="#"><i class="icon-google-plus google-plus"></i></a>
                    </div>
                  <hr />
                  <i class="icon-home"></i> &nbsp; 123, Some Area. Los Angeles, CA, 54321.
                  <hr />
                  <i class="icon-phone"></i> &nbsp; +239-3823-3434
                  <hr />
                  <i class="icon-envelope-alt"></i> &nbsp; <a href="mailto:#">someone@company.com</a>
                  <hr />
                  <div class="payment-icons">
                    <img src="${request.static_url('marketplace:static/img/payment/americanexpress.gif')}" alt="" />
                    <img src="${request.static_url('marketplace:static/img/payment/visa.gif')}" alt="" />
                    <img src="${request.static_url('marketplace:static/img/payment/mastercard.gif')}" alt="" />
                    <img src="${request.static_url('marketplace:static/img/payment/discover.gif')}" alt="" />
                    <img src="${request.static_url('marketplace:static/img/payment/paypal.gif')}" alt="" />
                  </div>
                </div>
              </div>

              <div class="col-md-4">
                <div class="widget">
                  <h5>About Us</h5>
                  <hr />
                   <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras elementum dolor eget nisi fermentum quis hendrerit magna vestibulum. Curabitur pulvinar ornare vulputate scelerisque scelerisque ut consectetur. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras elementum dolor eget nisi fermentum quis hendrerit magna vestibulum.</p>
                </div>
              </div>

              <div class="col-md-4">
                <div class="widget">
                  <h5>Links Goes Here</h5>
                  <hr />
                  <div class="two-col">
                    <div class="col-left">
                      <ul>
                        <li><a href="#">Condimentum</a></li>
                        <li><a href="#">Etiam at</a></li>
                        <li><a href="#">Fusce vel</a></li>
                        <li><a href="#">Vivamus</a></li>
                        <li><a href="#">Pellentesque</a></li>
                        <li><a href="#">Vivamus</a></li>
                      </ul>
                    </div>
                    <div class="col-right">
                      <ul>
                        <li><a href="#">Condimentum</a></li>
                        <li><a href="#">Etiam at</a></li>
                        <li><a href="#">Fusce vel</a></li>
                        <li><a href="#">Vivamus</a></li>
                        <li><a href="#">Pellentesque</a></li>
                        <li><a href="#">Vivamus</a></li>
                      </ul>
                    </div>
                    <div class="clearfix"></div>
                  </div>
                </div>
              </div>

            </div>

            <hr />
            <!-- Copyright info -->
            <p class="copy">Copyright &copy; 2012 | <a href="#">Your Site</a> - <a href="#">Home</a> | <a href="#">About Us</a> | <a href="#">Service</a> | <a href="#">Contact Us</a></p>
      </div>
    </div>
  <div class="clearfix"></div>
  </div>
</footer>

<!-- Footer ends -->


</body>
</html>
