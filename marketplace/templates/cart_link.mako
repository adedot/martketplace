

 <span>

  <!-- item details with price -->
  <a href="${request.route_url('cart')}" role="button" data-toggle="modal">
   % if 'count' in request.session:
        ${request.session['count']}
   %else:
        0
    %endif
    Item(s) in your <i class="icon-shopping-cart">
  </i></a> <span class="bold">

   % if 'sub_total' in request.session:
       $ ${request.session['sub_total']}
   %else:
       $ 0
    %endif
    </span>
</span>