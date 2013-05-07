/**
 * File - loader Konstuctor with ajax -request
 * @author Anja Siek <anja.marita@web.de>
 */
var File = function() {
};
/**
 * function to load file via Fileneame via ajax and return response
 * @author Anja Siek <anja.marita@web.de>
 * @param string filename
 * @return Object with 
 *      "status" 0 = OK 1 = error 
 *      "data" with return data
 */
File.prototype.loadfile = function (filename,type) {
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
        xmlHttp.open("GET",filename,false);
        //send request
        xmlHttp.send();
        // handel response if its done 
        if (xmlHttp.readyState == 4 ) {
            if (xmlHttp.status == 200) {
                response['status'] = 0;
                switch(type) {
                    case "xml":
                        response['data'] =  xmlHttp.responseXML; 
                        break;
                    case "text":
                        response['data'] =  xmlHttp.responseText;
                        break;
                    default:
                        response['data'] =  xmlHttp.response;
                }
            } else {
                response['data'] = xmlHttp.status + "error while loading file";
            }
            return response;
        }
    }
    return response;
};
 

