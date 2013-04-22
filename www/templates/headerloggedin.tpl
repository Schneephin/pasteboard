<div id="logo"><a href="/" ><%=header.title%></a></div>
<nav>
    <ul>
        <% for ( var i in header.nav ) { %>
            <li><a href="<%=header.nav[i].url%>"><%=header.nav[i].name%></a></li>
        <% } %>
    </ul>
</nav>
<div id="login-form">
    <p id="loggedintext">
        <%=header.loggedintext%>
        <span><%=name%></span>
        <button name="mydata"><%=header.mydata%></button>
        <button name="logout"><%=header.logout%></button>
    </p>
</div>
