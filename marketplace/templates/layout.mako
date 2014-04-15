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
    <!-- Check navbar -->
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/style.css')}">
    <link rel="stylesheet" href="${request.static_url('marketplace:static/css/red.css')}">
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
        <div class="social">
          <a href="#"><i class="icon-facebook facebook"></i></a>
          <a href="#"><i class="icon-twitter twitter"></i></a>
          <a href="#"><i class="icon-linkedin linkedin"></i></a>
          <a href="#"><i class="icon-google-plus google-plus"></i></a>
        </div>

                <!-- Logo. Use class "color" to add color to the text. -->
                  <div class="logo">
                    <h1><a href="${request.route_url('home')}">Allen Ikeja <span class="color bold">Marketplace</span></a></h1>

                  </div>
        </div>

        <div class="col-md-5 col-md-offset-3 pull-right">

          <!-- Search form -->
            <form class="form-inline" role="form" action="#" method="post" name="email">
			  <div class="form-group">
				<input type="email" class="form-control" id="email" placeholder="Email Address">
			  </div>

			  <button type="submit" class="btn btn-large">Subscribe</button>
			</form>

          <div class="hlinks">
           <!-- Use cart link -->
            <%include file="marketplace:templates/cart/cart_link.mako"/>

            <span>

            <!-- Add Checkout -->
            <a href="${request.route_url('checkout')}">Checkout</a>
            </span>


              <!-- Login and Register link -->
              <span class="lr"><a href="${request.route_url('login')}" role="button" data-toggle="modal">Login</a> or <a href="${request.route_url('register')}" role="button" data-toggle="modal">Register</a></span>

          </div>

        </div>

      </div>
    </div>
  </header>
  <!-- Header ends -->


   <!-- Navigation -->
          <div class="navbar bs-docs-nav" role="banner">

             <div class="container">
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
                   <li><a href="${request.route_url('category', id=1, slug='household')}">Household, Food, & Pets</a></li>
                   <li><a href="${request.route_url('category', id=2, slug='medicine')}">Medicine & Health</a></li>
                   <li><a href="${request.route_url('category', id=3, slug='vitamins')}">Vitamins</a></li>
                   <!-- li><a href="${request.route_url('category', id=4, slug='diet')}">Diet & Fitness</a></li -->
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
                    <div class="clearfix"></div>
                  </div>
                </div>
              </div>

            </div>

            <hr />
            <!-- Copyright info -->
            <p class="copy">Copyright &copy; 2012 |  <a href="${request.route_url('home')}">Home</a> | <a href="#">About Us</a> | <a href="#">Contact Us</a></p>
      </div>
    </div>
  <div class="clearfix"></div>
  </div>
</footer>

<!-- Footer ends -->


</body>
</html>
