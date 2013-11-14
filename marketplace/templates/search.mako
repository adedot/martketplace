<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<div class="span8"> <!--  Content-->
    <div class="input-group">
        <form action="/search" method="post" name="search">
            <input type="search" name="query" class="form-control"> 
            <span class="input-group-btn">
                <input class="btn btn-default" type="submit" value="Search" />
            </span>
        </form>
    </div>
</div> <!-- End of Content -->
<!-- Product Results-->
<div class="span5"> 
    <p>Product Results</p>
    <ul class="nav nav-pills nav-stacked">
    % for product in products:
    <li> <p>Name: <b>${product.name}</b></p></li>
    % endfor
    </ul>
</div>

