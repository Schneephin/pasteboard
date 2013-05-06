<h2></h2>
<table class="pastes">
    <caption><%=trans.tabletitle%></caption>
    <thead>
        <tr>
            <th><%=trans.pasteId%></th>
            <th><%=trans.pasteTitle%></th>
            <th><%=trans.pasteDate%></th>
        </tr>
    </thead>
    <tbody>
        <% for ( var i in pastes ) { %>
            <tr onclick='document.location ="/paste.py?id=<%=pastes[i].id%>"'>
                <td><%=pastes[i].id%></td>
                <td><%=pastes[i].title%></td>
                <td><%=pastes[i].date%></td>
            </tr>
        <% } %>
    </tbody>
</table>
