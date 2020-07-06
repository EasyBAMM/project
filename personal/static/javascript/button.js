window.onload = function() {
    var general, forward, left, stop, right, backward, cameraLeft, cameraRight;
    
    general = document.getElementById("toggle-button");
    forward = document.getElementById("forward");
    left = document.getElementById("left");
    stop = document.getElementById("stop");
    right = document.getElementById("right");
    backward = document.getElementById("backward");
    cameraLeft = document.getElementById("camera-left");
    cameraRight = document.getElementById("camera-right");

    var toggle = false;
    var sectionVideo = document.getElementById("video-section");
    var sectionCard = document.getElementById("card-section");
    sectionVideo.style.visibility = "hidden";
    sectionCard.style.visibility = "hidden";

    general.addEventListener("click", function(e) {
        toggle = !toggle;

        if(toggle == true){
            this.className = "btn btn-success btn-sm";
            this.innerHTML = "On";
            sectionVideo.style.visibility = "visible";
            sectionCard.style.visibility = "visible";
            controlHandle(e);        
        }
        else{
            this.className = "btn btn-danger btn-sm";
            this.innerHTML = "Off";
            sectionVideo.style.visibility = "hidden";
            sectionCard.style.visibility = "hidden";
            controlHandle(e);
        }
    });

    forward.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        carMove(e);
    }, false);

    forward.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(255,255,255)");
        carStop(e);
    }, false);

    left.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        carMove(e);
    }, false);

    left.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(255,255,255)");
        carStop(e);
    }, false);

    stop.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        carMove(e);
    }, false);

    stop.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(255,255,255)");
        carStop(stop);
    }, false);

    right.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        carMove(e);
    }, false);

    right.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(255,255,255)");
        carStop(e);
    }, false);

    backward.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        carMove(e);
    }, false);

    backward.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(255,255,255)");
        carStop(e);
    }, false);

    cameraLeft.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        cameraMove(e);
    }, false);

    cameraLeft.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(0, 183, 255)");
        cameraStop(e);
    }, false);

    cameraRight.addEventListener("mousedown", function(e) {
        changeButtonColor(e, "rgb(25,206,96)");
        cameraMove(e);
    }, false);

    cameraRight.addEventListener("mouseup", function(e){
        changeButtonColor(e, "rgb(0, 183, 255)");
        cameraStop(e);
    }, false);


    function changeButtonColor(e, color) {
        e.currentTarget.style.backgroundColor = color;
    }

    function controlHandle(e) {
        state = e.currentTarget.innerHTML;
        console.log(state);
        fetch("control?state=" + state)
        .then(response => response.text())
        .then(data => {
            //console.log(data);
        });
    }//controlHandle


    function carMove(e) {
        state = e.currentTarget.id;
        console.log(state);
        fetch("car?state=" + state)
        .then(response => response.text())
        .then(data => {
            //console.log(data);
        });
    }//carMove

    function carStop(e) {
        state = "stop";
        console.log(state);
        fetch("car?state=" + state)
        .then(response => response.text())
        .then(data => {
            //console.log(data);
        });
    }//carStop

    function cameraMove(e) {
        state = e.currentTarget.id;
        console.log(state);
        fetch("camera?state=" + state)
        .then(response => response.text())
        .then(data => {
            //console.log(data);
        });
    }//cameraMove

    function cameraStop(e) {
        state = "stop";
        console.log(state);
        fetch("camera?state=" + state)
        .then(response => response.text())
        .then(data => {
            //console.log(data);
        });
    }//cameraStop
};