//required for javascript pageloader see main.js function: loadScript  
//special javascript for paste page

/**
 * get data from api and add it via addToTemplate function to template rendering
 * @author Anja Siek
 * @author Christian Wenzlick 
 */
var token = readCookie('tk');

// loading is only done if the user is successfully logged in
if (typeof token != "undefined") {
    var data = new Object();
    data['tk'] = token; 
    var params = "data="+encodeURIComponent(JSON.stringify(data)) ;
    var rest = new Rest("POST", "api/pasteboard.py/getUser", "json", params);
    var result = rest.handleRequset();
    addToTemplate(result);
    
    var paste_id = readCookie('pasteid');
    deleteCookie('pasteid');

    //if a paste_id is defined load the paste and display it
    if(typeof paste_id != "undefined")
    {
        var data = new Object();
        data['paste_id'] = paste_id; 
        var params = "data="+encodeURIComponent(JSON.stringify(data));
        var rest = new Rest("POST", "api/pasteboard.py/getPasteById", "json", params);
        var result = rest.handleRequset();
        addToTemplate(result);
    }
  
    //add sidebar
   // var content = document.getElementById("contentouter");
   // content.classList.add("side");
   // content.classList.remove("noside");
    

    //add the codeEditor only after all the elements finished loading, else it will break
    function loadCodeEditor() {
    	var element = document.createElement("script");
 	element.src = "./../codemirrorBare/codeEditor.js";
 	document.body.appendChild(element);
    }

    if (window.addEventListener)
        window.addEventListener("load", loadCodeEditor, false);
    else if (window.attachEvent)
        window.attachEvent("onload", loadCodeEditor);
    else window.onload = loadCodeEditor;
}


/**
 * function createPaste
 * handles the paste creation form
 * @author Christian Wenzlick
 * @param form
 * @param page
 */
function createPaste(form, page) {
    editor.toTextArea()
    if (pruefeFormular(form)) {
	var result = handleForm(form, page);
        if (result["status"] == 0) {
            if (result["result"].state == 'ok') {
                if (null != result["result"].data.paste_id) {
                    this.document.location.href = "paste.py?id="+result["result"].data.paste_id;
                } else {
                    errorHandler.handel("failed");
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
}
