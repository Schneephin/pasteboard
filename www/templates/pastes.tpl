<!-- 
    template for pastes page
    this will be included in the content - div 
    and filled placeholders by micro-template.js 
-->
<h2><%=trans.tabletitle%></h2>
<div id="contentinner">
<table class="pastes">
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
                <td><%=pastes[i].paste_id%></td>
                <td><%=pastes[i].title%></td>
                <td><%=pastes[i].datum%></td>
            </tr>
        <% } %>
    </tbody>
</table>
</div>
