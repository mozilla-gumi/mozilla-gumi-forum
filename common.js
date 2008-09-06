function pvcheck() {
    if (document.post.PV.checked) {
        document.post.auca.disabled = true;
    } else {
        document.post.auca.disabled = false;
    }
}

