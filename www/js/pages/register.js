/**
 * function handleRegister
 * special handler for the register-form
 * @author Anja Siek <anja.marita@web.de>
 * @param form
 * @param page
 */
function handleRegister(form, page) {
    var result = handleForm(form, page);
    
    if (result["status"] == 0) {
        if (result["result"].state == 'ok') {
            if (null != result["result"].data.token) {
                this.document.location.href = "pastes.py?tk="+result["result"].data.token;
            } else {
                errorHandler.handel("failed to load data");n
            }
        } else {
            if (null != result["result"].msg) {
                errorHandler.handel(result["result"].msg);
            } else {
                errorHandler.handel("failed to load data");
            }
        }
    } else {
        errorHandler.handel("your register-Data was not correct");
    }
}
