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
 * function handleLogin
 * special handler for the login-form
 * @author Anja Siek <anja.marita@web.de>
 * @param form
 * @param page
 */
function handleLogin(form, page) {
    var result = handleForm(form, page);
    
    if (result["status"] == 0) {
        if (result["result"].state == 'ok') {
            if (null != result["result"].data.token) {
                this.document.location.href = "pastes.py?tk="+result["result"].data.token;
            } else {
                errorHandler.handel("failed to load data");n
            }
        } else {
            if (null != result["result"].msg) {n
                errorHandler.handel(result["result"].msg);
            } else {
                errorHandler.handel("failed to load data");
            }
        }
    } else {
        errorHandler.handel("your login-Data was not correct please register or try again");
    }
}

function invite()
{
    var rest = new Rest("POST", "api/pasteboard.py/getInviteKey", "json","");
    var result = rest.handleRequset(); 
    if (result["status"] == 0) {
        if (result["result"].state == 'ok') {
            if (null != result["result"].data.invkey ) {
                alert('inviteKey: '+ result["result"].data.invkey);
            }
        }
    }
}

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
/**
 * upstream code comes from:
 */
function setActive() {
  aObj = document.getElementById('header').getElementsByTagName('a');
  for(i=0;i<aObj.length;i++) {
    if(document.location.href.indexOf(aObj[i].href)>=0) {
      aObj[i].className='active';
    }
  }
}
