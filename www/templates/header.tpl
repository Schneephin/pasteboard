<div id="logo"><a href="/" ><%=header.title%></a></div>
<nav>
    <ul>
        <% for ( var i in header.nav ) { %>
            <li><a href="<%=header.nav[i].url%>"><%=header.nav[i].name%></a></li>
        <% } %>
    </ul>
</nav>

<div id="login-form">
<form onsubmit="handleLogin(this,\'login.py'); return false;">
    <input type="text" name="email" placeholder="<%=header.email%>">
    <input type="password" name="password" placeholder="<%=header.password%>">
    <input type="submit" value="<%=header.ok%>">
</form> 
</div>
