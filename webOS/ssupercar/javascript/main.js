window.onload = function () {
    // var bridge = new WebOSServiceBridge();
    // /*
    //  *  getTimeApi calls gettime of systemservice, a module in the platform.
    //  */
    // var getTimeApi = 'luna://com.webos.service.systemservice/clock/getTime';
    // var getTimeParams = '{}';

    // /*
    //  *  helloApi calls the hello method of js_service template provided by CLI.
    //  *  In this case, the service name is used as default name "com.domain.app.service" is.
    //  *  If you change this service name, you need to change the service name of the following API.
    //  *
    //  *  If you change the name to helloparmas as you want, the contents will be reflected on the screen.
    //  */
    // var helloApi = 'luna://com.domain.app.service/hello';
    // var helloParams = '{"name":"webOS"}';

    // function getTime_callback(msg) {
    //     var arg = JSON.parse(msg);
    //     if (arg.returnValue) {
    //         console.log("[APP_NAME: example web app] GETTIME_SUCCESS UTC : " + arg.utc);
    //         //webOSSystem.PmLogString(6, "GETTIME_SUCCESS", '{"APP_NAME": "example web app"}', "UTC : " + arg.utc);
    //     } else {
    //         console.error("[APP_NAME: example web app] GETTIME_FAILED errorText : " + arg.errorText);
    //         //webOSSystem.PmLogString(3, "GETTIME_FAILED", '{"APP_NAME": "example web app"}', "errorText : " + arg.errorText);
    //     }
    // }

    // function hello_callback(msg) {
    //     var arg = JSON.parse(msg);
    //     if (arg.returnValue) {
    //         document.getElementById("txt_msg").innerHTML = arg.Response;
    //         console.log("[APP_NAME: example web app] CALLHELLO_SUCCESS response : " + arg.Response);
    //         //webOSSystem.PmLogString(6, "CALLHELLO_SUCCESS", '{"APP_NAME": "example web app"}', "response : " + arg.Response);
    //     } else {
    //         console.error("[APP_NAME: example web app] CALLHELLO_FAILED errorText : " + arg.errorText);
    //         //webOSSystem.PmLogString(3, "CALLHELLO_FAILED", '{"APP_NAME": "example web app"}', "errorText : " + arg.errorText);
    //     }
    // }

    // bridge.onservicecallback = getTime_callback;
    // bridge.call(getTimeApi, getTimeParams);
    // document.getElementById("txt_msg").onclick = function () {
    //     bridge.onservicecallback = hello_callback;
    //     bridge.call(helloApi, helloParams);
    // };

    // var http = require('http');
    // var fs = require('fs');
    // var app = http.createServer(function (request, response) {
    //     var url = request.url;
    //     if (request.url == '/') {
    //         url = '/index.html';
    //     }
    //     if (request.url == '/favicon.ico') {
    //         response.writeHead(404);
    //         response.end();
    //         return;
    //     }
    //     response.writeHead(200);
    //     console.log(__dirname + url);
    //     response.end(fs.readFileSync(__dirname + url));

    // });
    // app.listen(3000);

    // const exec = require('child_process').exec;
    // exec('pwd', (err, stdout, stderr) => {
    //     if (err) {
    //         console.error(`exec error: ${err}`);
    //         return;
    //     }

    //     console.log(`stdout: ${stdout}`);
    //     console.log(`stderr: ${stderr}`);
    // });

    var url = document.location.href;
    var back, menu1, menu2, menu3, menu4, menu5;
    var status1 = false, 
        status2 = false;

    back = document.getElementById("back_key");
    
    menu1 = document.getElementById("menu_1");
    menu2 = document.getElementById("menu_2");
    menu3 = document.getElementById("menu_3");
    menu4 = document.getElementById("menu_4");
    menu5 = document.getElementById("menu_5");

    back.addEventListener("click", function(e) {
        location.replace("index.html");
    });

    menu1.addEventListener("click", function (e) {
        console.log(url + "menu1.html");
        location.replace("menu1.html");
    });
    menu2.addEventListener("click", function (e) {
        location.replace("menu2.html");
    });
    menu3.addEventListener("click", function (e) {
        location.replace("menu3.html");
    });
    menu4.addEventListener("click", function (e) {
        status1 = !status1;
        console.log("운전자 모니터링:" + status1);

        if (status1 == true)
            e.currentTarget.innerHTML = "운전자 모니터링: ON";
        else
            e.currentTarget.innerHTML = "운전자 모니터링: OFF";
    });
    menu5.addEventListener("click", function (e) {
        status2 = !status2;
        console.log("탑승자 케어 솔루션:" + status2);

        if (status2 == true)
            e.currentTarget.innerHTML = "운전자 모니터링: ON";
        else
            e.currentTarget.innerHTML = "운전자 모니터링: OFF";
    });

}