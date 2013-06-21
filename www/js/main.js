/**
 * class ErrorHandler 
 * @author Anja Siek <anja.marita@web.de>
 */
var ErrorHandler = function() {
    /**
     * function handel 
     * at the moment alert the error
     *
     * @param data
     * @return void
     */
    this.handel = function(data) {
        alert(data);
    }
};

/**
 * function handleForm
 * handels form data and uses rest handler to send data
 * via ajax
 * @author Anja Siek <anja.marita@web.de>
 * @param form
 * @param page
 * @return rest.result
 */
function handleForm(form, page) {

    var data = new Object();
    var elements  = form.elements;
    for(var i = 0; i < elements.length; i++) {
        data[elements[i].name] = elements[i].value;
    }

    var params = "data="+encodeURIComponent(JSON.stringify(data)) ;
    var rest = new Rest("POST", "api/" + page, "json", params);
    return rest.handleRequset();
}

/**
 * loadScript(url) 
 * function to load page js from url
 * @author Anja Siek <anja.marita@web.de>
 * @param url
 */
function loadScript(url)
{
    // adding the script tag to the head as suggested before
   var head = document.getElementsByTagName('head')[0];
   var script = document.createElement('script');
   script.type = 'text/javascript';
   script.src = url;

   // fire the loading
   head.appendChild(script);
}
/**
 * logout
 * function to log the user out from page
 * removes cookie with the login-token
 */
function logout()
{
    deleteCookie("tk");
    window.location.pathname = "";
}
/**
 * function addToTemplate
 * function to add data to template
 * @autor Anja Siek <anja.marita@web.de>
 * @param result
 */
function addToTemplate(result) {

    if (result["status"] == 0) { 
        if (result["result"].state == 'ok') {
            if (null != result["result"].data ) {
               template.addData(result["result"].data);
            }
        } else {
            deleteCookie("tk");
            window.location.pathname = "";
        }
    }
}
/**
 * upstream code comes from: http://www.quirksmode.org/js/cookies.html
 */
function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function deleteCookie(name)
{
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
/**
 * upstream code comes from:
 */
function setActive() {
  var aObj = document.getElementById('header').getElementsByTagName('a');
  for(var i=0;i<aObj.length;i++) {
    if(document.location.href.indexOf(aObj[i].href)>=0) {
      aObj[i].className='active';
    }
  }
}
