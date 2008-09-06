function emoticon(text) {
	var txtarea = document.post.comment;
	if(text == 'UA'){text="\n" + navigator.userAgent + "\n";}else{text = ' ' + text + ' ';}
	if (txtarea.createTextRange && txtarea.caretPos) {
		var caretPos = txtarea.caretPos;
		caretPos.text = caretPos.text.charAt(caretPos.text.length - 1) == ' ' ? caretPos.text + text + ' ' : caretPos.text + text;
		txtarea.focus();
	} else {
		txtarea.value  += text;
		txtarea.focus();
	}
}

function storeCaret(textEl) {
	if (textEl.createTextRange) textEl.caretPos = document.selection.createRange().duplicate();
}


function smileonoff(){
	if(document.post.smile.value == 'ON'){onoff='OFF';}else{onoff='ON';}
	document.post.smile.value = onoff;
	document.post.comment.focus();

}

/*
function dist{
	document.write('<span id="Linux" style="display:none;">ディストリビューション:<input type="text" name="Linux_" id="Linux_" size="10"></span>');
}
function ChangeSelection(selection, tid, tval) {
	if (selection.options[selection.selectedIndex].text == tval){
		document.getElementById(tid).style.display = "";
	} else {
		document.getElementById(tid).style.display = "none";
	}
}
*/
