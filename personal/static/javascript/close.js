window.onbeforeunload = function(e) {
    fetch("control?state=Off")
    .then(response => response.text())
    .then(data => {
        //console.log(data);
    });
};