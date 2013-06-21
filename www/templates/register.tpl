<!-- 
    template for register page
    this will be included in the content div
    and filled placeholders by micro-template.js 
-->
<h2><%=trans.registertitle%></h2>
<div id="contentinner">
    <div id ="info"><%=trans.text%></div>
    <div id="register-form">
        <form onsubmit="handleRegister(this,\'pasteboard.py/register'); return false;">
            <input class="test" type="text" name="name" placeholder="<%=trans.name%>">
            <input class="test" type="text" name="email" placeholder="<%=trans.header.email%>">
            <input class="test" type="password" name="password" placeholder="<%=trans.header.password%>">
            <input class="test" type="password" name="password-r" placeholder="<%=trans.passwordr%>">
            <input class="test" type="text" name="key" placeholder="<%=trans.key%>">
            <input type="submit" value="<%=trans.header.ok%>">
        </form> 
    </div>
</div>
