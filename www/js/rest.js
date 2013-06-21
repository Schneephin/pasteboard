/**
 * Rest - handler Constuctor with ajax -request
 *
 * @author Anja Siek <anja.marita@web.de>
 * @param string method (GET, POST)
 * @param string url
 * @param string type (xml,text,json)
 * @param string params 
 */
var Rest = function(method, url, type, params) {
    this.method = method;
    this.url = url;
    this.type = type;
    this.params = params;
};


Rest.prototype.loadfile = function (filename,type) {
    this.type = type;
    this.url = filename;
    return this.handleRequset();
}
/**
 * function to make a REST-handle via ajax and return response
 * @author Anja Siek <anja.marita@web.de>
 * @param string filename
 * @return Object with 
 *      "status" 0 = OK 1 = error 
 *      "data" with return data
 */
Rest.prototype.handleRequset = function () {
    var xmlHttp ;
    var response = new Object();
    
    response['status'] = 1;
    response['data'] = "unknown error";

    try {
        // Opera 8.0+, Firefox, Safari
        xmlHttp = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer Browsers
        try {
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Something went wrong
                return response;
            }
        }
    }
    // if object is sucsessfull created go on
    if (xmlHttp != null) {
        // open request
        xmlHttp.open(this.method,this.url,false);

        xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlHttp.setRequestHeader("Content-length", this.params.length);
        //send request
        xmlHttp.send(this.params);
        // handel response if its done 
        if (xmlHttp.readyState == 4 ) {
            if (xmlHttp.status == 200) {
                response['status'] = 0;
                switch(this.type) {
                    case "xml":
                        response['result'] =  xmlHttp.responseXML; 
                        break;
                    case "text":
                        response['result'] =  xmlHttp.responseText;
                        break;
                    case "json":
                        response['result'] =  JSON.parse(xmlHttp.responseText);
                        break;
                    default:
                        response['result'] =  xmlHttp.response;
                }
            } else {
                response['result'] = xmlHttp.status + "error while loading file";
            }
            return response;
        }
    }
    return response;
};
 

