<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<!-- Add login Form-->
<div class="span5">
    <hr>
    <h4>User Login</h4>


    <form action="." method="post">

        <label for="login">Email</label>
        <p> ${form.email()} </p><br/>
        <label for="password">Password</label>
        <p> ${form.password()} </p>
        <input type="submit" name="form.submitted"
               value="Log In"/>
    </form>
</div>