window.onload = function() {

    var fromFrame = document.getElementById("iframe").contentWindow.document;
    // var some = fromFrame.getElementById("ss");
    var water_in, water_out, water_stop;
    var trafficlight1_red, trafficlight1_green;
    var trafficlight2_red, trafficlight2_green;
    var waterhose_in, waterhose_out, waterhose_stop;
    var car1_stop, car1_forward, car2_stop, car2_forward;
    var robotarm_servo1, robotarm_servo2, robotarm_servo3, robotarm_servo4;    
    
    water_in = fromFrame.getElementById("water-in");
    water_out = fromFrame.getElementById("water-out");
    water_stop = fromFrame.getElementById("water-stop");
    
    trafficlight1_red = fromFrame.getElementById("trafficlight1-red");
    trafficlight1_green = fromFrame.getElementById("trafficlight1-green");
    trafficlight2_red = fromFrame.getElementById("trafficlight2-red");
    trafficlight2_green = fromFrame.getElementById("trafficlight2-green");
    
    waterhose_in = fromFrame.getElementById("waterhose-in");
    waterhose_out = fromFrame.getElementById("waterhose-out");
    waterhose_stop = fromFrame.getElementById("watrehose-stop");
    
    car1_stop = fromFrame.getElementById("car1-stop");
    car1_forward = fromFrame.getElementById("car1-start");
    car2_stop = fromFrame.getElementById("car2-stop");
    car2_forward = fromFrame.getElementById("car2-start");  
    
    robotarm_servo1 = fromFrame.getElementById("servo-1");
    robotarm_servo2 = fromFrame.getElementById("servo-2");
    robotarm_servo3 = fromFrame.getElementById("servo-3");
    robotarm_servo4 = fromFrame.getElementById("servo-4");
    
    var url_water, url_trafficlight1, url_trafficlight2, url_waterhose, url_car1, url_car2, url_robotarm;
    
    url_water = fromFrame.getElementById("url-water");
    url_trafficlight1 = fromFrame.getElementById("url-trafficlight1");
    url_trafficlight2 = fromFrame.getElementById("url-trafficlight2");
    url_waterhose = fromFrame.getElementById("url-waterhose");
    url_car1 = fromFrame.getElementById("url-car1");
    url_car2 = fromFrame.getElementById("url-car2");
    url_robotarm = fromFrame.getElementById("url-robotarm");

    water_in.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_water.innerHTML + "/water-in");
        let url = url_water.innerHTML + "/water-in";
        fetchData(url);
    });

    water_out.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_water.innerHTML + "/water-out");
        let url = url_water.innerHTML + "/water-out";
        fetchData(url);
    });

    water_stop.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_water.innerHTML + "/water-stop");
        let url = url_water.innerHTML + "/water-stop";
        fetchData(url);
    });

    trafficlight1_red.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_trafficlight1.innerHTML + "/red");
        let url = url_trafficlight1.innerHTML + "/trafficlight1-red";
        fetchData(url);
    });

    trafficlight1_green.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_trafficlight1.innerHTML + "/green");
        let url = url_trafficlight1.innerHTML + "/trafficlight1-green";
        fetchData(url);
    });

    trafficlight2_red.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_trafficlight2.innerHTML + "/red");
        let url = url_trafficlight2.innerHTML + "/trafficlight2-red";
        fetchData(url);
    });

    trafficlight2_green.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_trafficlight2.innerHTML + "/green");
        let url = url_trafficlight2.innerHTML + "/trafficlight2-green";
        fetchData(url);
    });

    waterhose_in.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_waterhose.innerHTML + "/waterhose-in");
        let url = url_waterhose.innerHTML + "/waterhose-in";
        fetchData(url);
    });

    waterhose_out.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_waterhose.innerHTML + "/waterhose-out");
        let url = url_waterhose.innerHTML + "/waterhose-out";
        fetchData(url);
    });
    
    waterhose_stop.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_waterhose.innerHTML + "/waterhose-stop");
        let url = url_waterhose.innerHTML + "/waterhose-stop";
        fetchData(url);
    });

    car1_stop.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_car1.innerHTML + "/car1_stop");
        let url = url_car1.innerHTML + "/car1-stop";
        fetchData(url);
    });

    car1_forward.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_car1.innerHTML + "/car1_forward");
        let url = url_car1.innerHTML + "/car1-forward";
        fetchData(url);
    });

    car2_stop.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_car2.innerHTML + "/car2_stop");
        let url = url_car2.innerHTML + "/car2-stop";
        fetchData(url);
    });

    car2_forward.addEventListener('click', function(event){
        alert('Hello world, '+ event.target.id);
        // console.log(url_car1.innerHTML + "/car1_forward");
        let url = url_car2.innerHTML + "/car2-forward";
        fetchData(url);
    });

    robotarm_servo1.addEventListener('change', function(event){
        // alert('Hello world, '+ event.target.id);
        console.log(event.target.value);
        // console.log(url_robotarm.innerHTML + "/servo-1?value=" + event.target.value);
        let url = url_robotarm.innerHTML + "/servo-1?value=" + event.target.value;
        fetchData(url);
    });

    robotarm_servo2.addEventListener('change', function(event){
        // alert('Hello world, '+ event.target.id);
        console.log(event.target.value);
        // console.log(url_robotarm.innerHTML + "/servo-2?value=" + event.target.value);
        let url = url_robotarm.innerHTML + "/servo-2?value=" + event.target.value;
        fetchData(url);
    });

    robotarm_servo3.addEventListener('change', function(event){
        // alert('Hello world, '+ event.target.id);
        console.log(event.target.value);
        // console.log(url_robotarm.innerHTML + "/servo-3?value=" + event.target.value);
        let url = url_robotarm.innerHTML + "/servo-3?value=" + event.target.value;
        fetchData(url);
    });

    robotarm_servo4.addEventListener('change', function(event){
        // alert('Hello world, '+ event.target.id);
        console.log(event.target.value);
        // console.log(url_robotarm.innerHTML + "/servo-4?value=" + event.target.value);
        let url = url_robotarm.innerHTML + "/servo-4?value=" + event.target.value;
        fetchData(url);
    });


    function fetchData(url) {
        console.log("fetch: " + url);
        // fetch(url)
        // .then(response => response.text())
        // .then(data => {
        //     //console.log(data);
        // });
    }
};