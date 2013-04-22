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
