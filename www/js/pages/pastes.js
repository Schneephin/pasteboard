//required for javascript pageloader see main.js function: loadScript  
//special javascript for pastes page

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

    var rest = new Rest("POST", "api/pasteboard.py/getAllCategorys", "json", params);
    var result = rest.handleRequset();
    addToTemplate(result);

    data['cat'] = "0"; 
    var params = "data="+encodeURIComponent(JSON.stringify(data)) ;
    var rest = new Rest("POST", "api/pasteboard.py/getPastesList", "json", params);
    var result = rest.handleRequset();
    addToTemplate(result);

}

function filterPastes(categoryid)
{
    data['cat'] = categoryid;
    var params = "data="+encodeURIComponent(JSON.stringify(data)) ;
    var rest = new Rest("POST", "api/pasteboard.py/getPastesList", "json", params);
    var result = rest.handleRequset();
    addToTemplate(result);
    template.render("pastes","content");
}
