<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      xmlns:tal="http://xml.zope.org/namespaces/tal"
      metal:define-macro="layout" lang="en">
<head>
    <title>${title}</title>
    <more metal:define-slot="head-more"></more>



    <link rel="stylesheet"
          href="${request.static_url('marketplace:static/bootstrap/css/bootstrap-responsive.css')}" />
     <link rel="stylesheet"
      href="${request.static_url('marketplace:static/bootstrap/css/bootstrap.min.css')}"/>
    <script src="http://code.jquery.com/jquery.js"></script>
    <script src="${request.static_url('marketplace:static/bootstrap/js/bootstrap.min.js')}"></script>
</head>
<body>
 <div id="main" class="container">

  <div class="masthead">
  <h1>The Baker's World Store</h1>
  <div class="navbar">
    
    <div class="navbar-inner">

      <ul class="nav">
      	
      	<li></li>
        <li><a href="#">Home</a></li>
        <li><a href="#">New Products</a></li>
        <li><a href="#">My Account</a></li>
        <li><a href="#">Shopping Cart</a></li>
        <li><a href="#">Checkout</a></li>
      </ul>

    </div>
    </div>
  </div>

  <div class="row">
         <div class="span4">
             <div class="well sidebar-nav">
            <ul class="nav">
              <li><a href="#">Cakes</a></li>
              <li><a href="#">Vitamins</a></li>
              <li><a href="#">Snacks</a></li>
              <li><a href="#">Prescriptions</a></li>
            </ul>
          </div><!--/.well -->
         </div>

     <div class="bottom">
        ${next.body()}
      </div>
   </div>


  </div>

</body>
</html>