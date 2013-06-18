<h2 style=""  onclick="filterPastes('<%= 0 %>');" ><%=trans.sidebar%></h2>
<% function printCats(cats, categorys, iter) { %>
    <ul>
        <% for ( var i in cats ) { %>
           <li >
                <p style="padding-left:<%=iter%>px;" onclick="filterPastes('<%=i %>');"><%=cats[i]%></p>
                <% if (null != categorys[i] ) {
                    printCats(categorys[i], categorys,(iter+10));
                } %>
            </li>
        <% } %>
    </ul>
<% } %>
<div id="sidenav">
<% printCats(categorys[0], categorys, 10); %>
</div>
