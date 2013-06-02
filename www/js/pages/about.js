//required for javascript pageloader see main.js function: loadScript  
//special javascript for about page

/**
 * get data from api and add it via addToTemplate function to template rendering
 */
var token = readCookie('tk');

//only if user is logged in we can load data
if (typeof token != "undefined") {
    var data = new Object();
    data['tk'] = token; 
    var params = "data="+encodeURIComponent(JSON.stringify(data)) ;
    var rest = new Rest("POST", "api/pasteboard.py/getUser", "json", params);
    var result = rest.handleRequset();
    addToTemplate(result);
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
                errorHandler.handel("failed to load data");
            }
        } else {
            if (null != result["result"].msg) {
                errorHandler.handel(result["result"].msg);
            } else {
                errorHandler.handel("failed to load data");
            }
        }
    } else {
        errorHandler.handel("your login-Data was not correct please register or try again");
    }
}
