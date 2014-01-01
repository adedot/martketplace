<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>


<div class="span5"> <!--  Content-->
    <div class="input-group">
     <form action="${request.route_url('register')}" method="post">

               <p> Email:        ${form.email()} </p>
               <p>Phone:        ${form.phone()} </p>

                <p> First Name:        ${form.first_name()} </p>
                <p> Last Name:        ${form.last_name()} </p>
               <p>Password:     ${form.password()} </p>
               <p>Confirmed Password:     ${form.confirm()} </p>
               <p>Rx/Prescription Number:   ${form.prescription_number()} </p>

               <input type="submit" name="form.submitted"
               value="Register"/>
      </form>
     </div>

</div>