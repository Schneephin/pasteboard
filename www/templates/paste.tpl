<!-- 
    template for paste page
    this will be included in the content - div
    and filled placeholders by micro-template.js 
-->
<h2><%=trans.createPaste%></h2>
<div id="contentinner">
<div id="paste-form">
<form onsubmit="createPaste(this,\'pasteboard.py/createPaste'); return false;">
    <p><%=trans.pasteTitle%>:</p><p><input type="text" name="title" placeholder="<%=trans.pasteTitle%>"></p>
    <p><%=trans.pasteCategory%>:</p><p><input type="text" name="category" placeholder="<%=trans.pasteCategory%>"></p>
    <p><%=trans.pasteContent%>:</p><p><textarea name="content" rows="30" cols="60"></textarea></p>
    <input type="submit" value="<%=trans.pasteSubmit%>">
</form> 
</div>
</div>





