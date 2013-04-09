<div id="logo"><a href="#" ><%=header.title%></a></div>
<nav>
    <ul>
        <% for ( var i in header.nav ) { %>
            <li><a href="<%=header.nav[i].url%>"><%=header.nav[i].name%></a></li>
        <% } %>
    </ul>
</nav>
