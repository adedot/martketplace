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
                   <li><a href="${request.route_url('category', id=1, slug='wine')}">Wine</a></li>
                   <li><a href="${request.route_url('category', id=2, slug='cake')}">Cakes</a></li>
                   <li><a href="${request.route_url('category', id=3, slug='electronics')}">Electronics</a></li>
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
<div id="footer">
      <div class="container">
        <p class="text-muted">© 2014 Ade Labs </p>
      </div>
    </div>

<!-- Footer ends -->


</body>
</html>
