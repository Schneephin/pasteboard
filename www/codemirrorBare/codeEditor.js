/*
*	codeEditor
*	Provides a code editor with syntax highlight and automated language detection
*	@author: Christian Wenzlick <christian.wenzlick@siemens.com>
*/

	// load all scripts and css files required for codemirror
	loadExternalScripts();

	var modes;
	var rootElement;
	var detectionLabel;
	var select;
	var button;
	var texteditor;
	var editor
	
	/*
	*	Initialise the code editor instance and attach it to the codeeditor div
	*	@author cwe
	*/
	function initialiseCodeEditor()
	{ 
		// sets the path were language modes can be found - %N represents a mode like 'php'
		CodeMirror.modeURL = "../mode/%N/%N.js"; 
		modes = CodeMirror.modeInfo;
		
		// get the codeeditor div and create all visual elements
		rootElement = document.getElementById("codeeditor");
		detectionLabel = document.createElement("label");
		select = document.createElement("select");
		button = document.createElement("button");
		//texteditor = document.createElement("textarea");
		//texteditor.id = "codeMirrorEditor";
		
                // fill the select box with all available modes
		fillLanguageSelect();
		
                // insert all visual elements into the dom tree
		rootElement.parentNode.insertBefore(button, rootElement);
		rootElement.parentNode.insertBefore(select, button);
		rootElement.parentNode.insertBefore(detectionLabel, select);
		//rootElement.parentNode.insertBefore(texteditor, detectionLabel);

		detectionLabel.innerHTML = "Detecting: ";
		
		button.innerHTML = 'Ausw&auml;hlen';
		button.onclick = function(){
			endDetection(); return false;
		};
		
		/*
		*	defines the codeMirrorEditor element as the standard editor and sets options:
		*	lineNumbers: true -	show line numbers 
		*	viewportMargin: Infinity - auto resize the editor
		* 	mode: "null" - initial mode is null, as in no highlight
		*/
		editor = CodeMirror.fromTextArea(document.getElementById("codeMirrorEditor"), { lineNumbers: true, viewportMargin: Infinity, mode: "null" });
		
		// preload all available modes
		for(var n = 0; n < modes.length; n++)
		{	
			CodeMirror.autoLoadMode(editor, modes[n].mode);
		}
		
		// register the determinLanguage function on "change" events of the editor
		editor.on("change", determineLanguage);
	}
	
	/*
	*	Load all external scripts and css files for codemirror
	*	@author cwe
	*/
	function loadExternalScripts()
	{ 
		loadExternalCSS("./codemirrorBare/lib/codemirror.css");
		loadExternalJavaScript("./codemirrorBare/lib/codemirror.js");
		loadExternalJavaScript("./codemirrorBare/mode/meta.js");
		loadExternalJavaScript("./codemirrorBare/addon/mode/loadmode.js");
		loadExternalJavaScript("./codemirrorBare/addon/runmode/runmode.js", true);
	}
	
	/*
	*	Load an external css file
	*	@param filename - filename and path of the css file
	*	@author cwe
	*/
	function loadExternalCSS(filename)
	{
		var css = document.createElement("link")
		css.rel = "stylesheet";
		css.type = "text/css";
		css.href = filename;
		// add the css element to the head if available or the body
		(document.getElementsByTagName('HEAD')[0]||document.body).appendChild(css);
	}
	
	/*
	*	Load an external javascript file
	*	@param filename - filename and path of the js file
	*	@param last - set if the current file is the last one to load, defaults to false
	*	@author cwe
	*/
	function loadExternalJavaScript(filename, last = false)
	{
		var script = document.createElement('script');
		script.async = false;
		script.src = filename;
		script.type = "text/javascript";
		// if this is the last file then add the initialise function to the onload event
		if(last == true)
		{ 
			script.onload = initialiseCodeEditor;
		}
		// add the script tag to the head if available or the body
		(document.getElementsByTagName('HEAD')[0]||document.body).appendChild(script);
	}
	
	/*
	* Fill the select element with all available language modes
	* @author cwe
	*/
	function fillLanguageSelect()
	{
		for(var i = 0; i < modes.length; i++)
		{
			select.options.add(new Option(modes[i].mime));
		}
	}
	
	/*
	* Ends the automated language detection
	* @author cwe
	*/
	function endDetection()
	{
		// removes the event handler and sets the editor mode to the selected value
		editor.off("change", determineLanguage);
		editor.setOption("mode", select.value);
		detectionLabel.innerHTML = "Selected: ";
	}
	
	/*
	* Try to determine the editor language 
	* Basically the function tries to highlight the editor with every available mode and counts the found "highlight-elements". Modes with low scores are discared until eventually only one mode remains.
	* There is no guaranty that the correct language will be determined with this approach, especially for mode groups that are quite similar like c/c++/c#, but it is a reasonably close and fast way.
	* @author cwe
	*/
	function determineLanguage() {
		// get the current editor text
		var input = editor.getValue();
		
		// detection of text below 50 chars is pretty bad, so leave here
		if(input.length < 50)return;
					
		var modeInput;
		var count = 0;
		var countCurrentWinner = 0;
		var currentWinner = "";
		
		/*
		*	callback function for the runMode function
		*	this function is called each time the runMode function finds a match (null counts as well) for a text part
		*	@param text - the current text part
		*	@param style - the style for the current text
		*	@author cwe
		*/
		function countHits(text, style)
		{	
			// count if the current element has a style which is not null and not one of the trivial styles comment, string...
			if(style != null && style != "comment" && style != "string" && style != "variable" && style != "bracket" && style != "property error")
			{
				count++;
			}
		}
		var m = modes;
		document.getElementById("results").value = "";
		
		// try highlighting for every mode in the modes array
		for(var i = 0; i < modes.length; i++)
		{
			count = 0;
			// runMode takes an input and mode and runs the syntax highlighting of codemirror. the third parameter in this case is a callback function that gets called with every hit
			CodeMirror.runMode(input, modes[i].mime, countHits);
			document.getElementById("results").value += modes[i].mime + " - " + count + "\r\n";
			
			// checks if the current mode scores higher than the winner 
			if(count > countCurrentWinner)
			{
				countCurrentWinner = count;
				currentWinner = modes[i];
			}
			// if the current mode scores lower than 5% of the input length it is discarded
			else if(count < input.length *5/100) 
			{
				modes[i] = null;
			}
			
		}
		// removes all empty elements from the modes array
		modes = modes.filter(function(element){return element !== null});
		// if there is a winner with a score > 0
		if(currentWinner.mode != "" && countCurrentWinner > 0)
		{
			modeInput = currentWinner;
			// if there is only one mode left end detection
			if(modes.length == 1)
			{
				select.value = modeInput.mime;
				editor.off("change", determineLanguage);
				detectionLabel.innerHTML = "Selected: ";
			}
			// if there are still modes left continue detecten and set the current winner as "preferred" mode
			else
			{
				detectionLabel.innerHTML = "Detecting: ";
				select.value = modeInput.mime;
			}
		}
		
		// set the winner mode
		editor.setOption("mode", modeInput.mime);
		CodeMirror.autoLoadMode(editor, modeInput.mode);
	}
