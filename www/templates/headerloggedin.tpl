<div id="logo"><a href="/" ><%=trans.header.title%></a></div>
<nav>
    <ul>
        <% for ( var i in trans.header.nav ) { %>
            <li><a href="<%=trans.header.nav[i].url%>"><%=trans.header.nav[i].name%></a></li>
        <% } %>
    </ul>
</nav>
<div id="login-form">
    <p id="loggedintext">
        <%=trans.header.loggedintext%>
        <span><%=username%></span>
        <button name="mydata"><%=trans.header.mydata%></button>
        <button name="logout" onclick="logout();"><%=trans.header.logout%></button>
    </p>
</div>
