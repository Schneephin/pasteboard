/**
 * handle Page and there templates
 * @author Anja Siek <anja.marita@web.de>
 * @param Object pages
 */
function pageHandle(pages) {
    // get page
    var page = window.location.pathname;
    page = page.replace(/\.[^/.]+$/, "");
    page = page.replace("/", "");
    if (page == "") { 
        var page = "home";
    }
    // get search-values and language
    var lang = "de";
    var search = handleSearch();
    if (null != search['lang'] ) {
        lang = search['lang'];
    }
    //create handel templates
    var template = new Template(page,lang);  
    for (i in pages) {
        handleTemplate(template,pages[i],i);
    }
};

/**
 * function handleTemplate
 * handels content loading and templating of Template
 * @author Anja Siek <anja.marita@web.de>
 * @param Object template
 * @param string page
 * @param string id
 */
function handleTemplate(template, page, id) {
    var returnv = template.load(page);
    if (returnv) {
        template.render(page,id);
    }
}

/**
 * handleSearch()
 * @author Anja Siek <anja.marita@web.de>
 * handels search ($_GET params from url)
 * @return Object result
 */
function handleSearch(){
    var result = {};

    if (window.location.search) {
        //split up the query string and store in an associative array
        var params = window.location.search.slice(1).split("&");
        for (var i = 0; i < params.length; i++) {
            var tmp = params[i].split("=");
            result[tmp[0]] = unescape(tmp[1]);
        }
    }
    return result;
}
