//required for javascript pageloader see main.js function: loadScript  
//special javascript for home page

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
/**
 * function invite
 * function to get invitekey from api
 * @author Anja Siek <anja.marita@web.de
 */
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
