function pvcheck() {
    if (document.post.PV.checked) {
        document.post.auca.disabled = true;
    } else {
        document.post.auca.disabled = false;
    }
}

function add_linkify(link) {
    var com_box = document.getElementById("comment");
    com_box.value += " " + link + " ";
    com_box.focus();
}

