<!-- extend home base layout -->
<%inherit file="marketplace:templates/layout.mako"/>

<!-- Add login Form-->
<div class="span5">
    <hr>
    <h4>Login</h4>
    <span tal:replace="message"/>

    <form action="${url}" method="post">
        <input type="hidden" name="came_from"
               value="${came_from}"/>
        <label for="login">Username</label>
        <input type="text" id="login"
               name="login"
               value="${login}"/><br/>
        <label for="password">Password</label>
        <input type="password" id="password"
               name="password"
               value="${password}"/><br/>
        <input type="submit" name="form.submitted"
               value="Log In"/>
    </form>
</div>