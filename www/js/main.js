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
 

/**
 * Template constructor
 * This object can load and render templates and will save them.
 * @author Anja Siek <anja.marita@web.de>
 */
var Template = function(page, lang) {
    this.file = new File;
    this.data = this.getTranslations(page, lang);
    this.templatesDir = "templates";
    this.templates =  new Array();
    this.html  = "";
};             

/**
 * getTranslation function 
 * load Translations from xml file
 *
 * @author Anja Siek <anja.marita@web.de>
 * @param string page      // witch page should be loaded
 * @param string lang      // for witch language 
 * @return array data 
 */
Template.prototype.getTranslations = function(page, lang) {
    

    var file = "languages/" + lang + "/"+ page + ".xml";
    alert("lol");
    var respronse = this.file.loadfile(file, "xml");

    switch (respronse['status']) {
        case  0 :
            var trans = respronse['data'];
            break;
        case 1 :
            ErrorHandler.handel(respronse['data']);
            break;
    }

    var data = xml2array(trans);
    return data;
};


/**
 * load function
 * load the template from file
 *
 * @author Anja Siek <anja.marita@web.de> 
 * @uses ErrorHandler
 * @param string name       // whitch template 
 * @return boolean
 */
Template.prototype.load = function(name) {
    var file =  this.templatesDir + "/" + name + ".tpl";
    var respronse = this.file.loadfile(file, "text");

    switch (respronse['status']) {
        case  0 :
            var html = respronse['data'];
            var template = new Object();
            template["file"] = file;
            template["html"] = html;
            this.templates[name] = template;
            return true;
            break;
        case 1 :
            ErrorHandler.handel(respronse['data']);
            return false;
            break;
    }
    return false;
};

/**
 * render function
 * renders template into html with micro-template functionality
 *
 * @author Anja Siek <anja.marita@web.de>
 * @uses ErrorHandler
 * @param string name       //name of the template
 * @param string id         // id of html-element
 */
Template.prototype.render = function(name, id){

    if (typeof this.templates[name] == "object" ) {
        var results = document.getElementById(id);
        results.innerHTML = tmpl(this.templates[name]["html"], this.data);
    } else {
        ErrorHandler.handel("can not render Template");
    }
};


/**
 * class ErrorHandler 
 * @author Anja Siek <anja.marita@web.de>
 */
var ErrorHandler = function() {
    /**
     * function handel 
     * at the moment alert the error
     *
     * @param data
     * @return void
     */
    this.handel = function(data) {
        alert(data);
    }
};

var ErrorHandler = new ErrorHandler;
