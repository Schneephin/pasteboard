<!DOCTYPE html>
<!-- 
    main layout for all pages 
-->
<html lang="de">
    <head>
        <meta charset="utf-8" /> 
        <title>pasteboard ()</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
        <script src="js/micro-template.js"></script>
        <script src="js/xml2array.js"></script>
        <script src="js/pageHandler.js"></script>
        <script src="js/rest.js"></script>
        <script src="js/template.js"></script>
        <script src="js/main.js"></script>
        <script src="js/formulare.js"></script>
     </head>
    <body>
        <div id="container">
            <header id="header"></header>
            <div id="contentouter"><section id="content"></section></div>
            <aside id="sidebar"></aside>
            <footer id="footer"></footer>
        </div>
        <script type="text/javascript">
            var template,errorHandler ;
            // on document ready: 
            document.addEventListener('DOMContentLoaded', function () {{
                // initalize template and errorhandler objects
                errorHandler = new ErrorHandler();
                template = new Template();  
                // handle pages it will be filled via python template handling
                pageHandle( {} );
                // check active page
                setActive();
                
            }}, false);
        </script>
    </body>
</html>
