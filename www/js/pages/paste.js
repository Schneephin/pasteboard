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
    
    //add sidebar
    var content = document.getElementById("contentouter");
    content.classList.add("side");
    content.classList.remove("noside");

}
