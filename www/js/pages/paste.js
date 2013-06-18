//required for javascript pageloader see main.js function: loadScript  
//special javascript for paste page

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
