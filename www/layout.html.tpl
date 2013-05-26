<!DOCTYPE html>
<html lang="de">
    <head>
        <meta charset="utf-8" /> 
        <title>pasteboard ()</title>
        <link rel="stylesheet" href="css/main.css" type="text/css" />
        <script src="js/micro-template.js"></script>
        <script src="js/xml2array.js"></script>
        <script src="js/pageHandler.js"></script>
        <script src="js/file.js"></script>
        <script src="js/rest.js"></script>
        <script src="js/template.js"></script>
        <script src="js/main.js"></script>
        <script src="js/formulare.js"></script>
     </head>
    <body>
        <div id="container">
            <header id="header"></header>
            <section id="content"></section>
            <aside id="sidebar"></aside>
            <footer id="footer"></footer>
        </div>
        <script type="text/javascript">
            document.addEventListener('DOMContentLoaded', function () {{
                errorHandler = new ErrorHandler();
                template = new Template();  
                pageHandle( {} );
                setActive();
                
            }}, false);
        </script>
    </body>
</html>
