<div id="logo"><a href="/" ><%=trans.header.title%></a></div>
<nav>
    <ul>
        <% for ( var i in trans.header.nav ) { %>
            <li><a href="<%=trans.header.nav[i].url%>"><%=trans.header.nav[i].name%></a></li>
        <% } %>
    </ul>
</nav>

<div id="login-form">
<form onsubmit="handleLogin(this,\'pasteboard.py/login'); return false;">
    <input type="text" name="email" placeholder="<%=trans.header.email%>">
    <input type="password" name="password" placeholder="<%=trans.header.password%>">
    <input type="submit" value="<%=trans.header.ok%>">
</form> 
</div>
