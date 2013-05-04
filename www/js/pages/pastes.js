function addToTemplate(result) {

    if (result["status"] == 0) { 
        if (result["result"].state == 'ok') {
            if (null != result["result"].data ) {
               template.addData(result["result"].data);
            }
        }
    }
}
 
var token = readCookie('tk');
var data = new Object();
data['tk'] = token; 
var params = "data="+encodeURIComponent(JSON.stringify(data)) ;

var rest = new Rest("POST", "api/pasteboard.py/getUser", "json", params);
var result = rest.handleRequset();
addToTemplate(result);

var rest = new Rest("POST", "api/pasteboard.py/getPastesList", "json", params);
var result = rest.handleRequset();
addToTemplate(result);
