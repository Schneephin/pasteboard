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

var ErrorHandler = new ErrorHandler;




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
        if (null != result["data"].token) {
            this.document.location.href = "loggedin.py?tk="+result["data"].token;
        } else {
            alert(result["data"].error);
        }
    } else {
        alert("your login-Data was not correct please register or try again");
    }
}
