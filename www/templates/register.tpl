<div id ="info"><%=trans.text%></div>
<div id="register-form">
<form onsubmit="handleRegister(this,\'pasteboard.py/register'); return false;">
    <input type="text" name="name" placeholder="<%=trans.name%>">
    <input type="text" name="email" placeholder="<%=trans.header.email%>">
    <input type="password" name="password" placeholder="<%=trans.header.password%>">
    <input type="password" name="password-r" placeholder="<%=trans.passwordr%>">
    <input type="text" name="key" placeholder="<%=trans.key%>">
    <input type="submit" value="<%=trans.header.ok%>">
</form> 
</div>
