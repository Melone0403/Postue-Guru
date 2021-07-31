//Global Variables
var allBtns = document.querySelectorAll("button");

window.onload = function() {
    var button = document.getElementById("toggleCam");
    var camera = document.getElementById("bg");
    button.innerHTML = "Show Preview";
    camera.style.display = "none";
};

//toggleCode:
function togglePreview() {
    var button = document.getElementById("toggleCam");
    var camera = document.getElementById("bg");

    if (camera.style.display === "none") {
        loadPython();
        button.innerHTML = "End Preview";
        camera.style.display = "block";
    } 
    else {
        vidOff();
        button.innerHTML = "Setup";
        camera.style.display = "none";
    }
    return true;
}

async function vidOn()
{
    //getMedia({audio: true, video: true});
    // Get access to the camera!
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding `{ audio: true }` since we only want video now
        let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        video.srcObject = stream;
    }
}

function vidOff() {
    var video = document.querySelector("#bg");
    video.remove();
}
////////////////////////////////////////////////////

//Timer
//Define vars to hold time values
let seconds = 0;
let minutes = 0;
let hours = 0;

//Define vars to hold display value
let displaySeconds = 0;
let displayMinutes = 0;
let displayHours = 0;

//Define var to hold set interval function
let interval = null;

//Define a stop timer
let timeFreq = 100;

//Break Flag
let breakFlag = false;

//stopwatch status
let status = "stopped";

function stopWatch(){
    seconds++;
    if(seconds/60 == 1){
        seconds = 0;
        minutes++;
        if(minutes/60 == 1){
            minutes = 0;
            hours++;
            
        }
    }
    if(seconds < 10){
        displaySeconds = "0"+seconds.toString();
    }
    else{
        displaySeconds = seconds;
    }
    if(minutes < 10){
        displayMinutes = "0"+minutes.toString();
    }
    else{
        displayMinutes = minutes;
    }
    if(minutes >= timeFreq){
        breakFlag = true;
    }
    else{
        displayMinutes = "0"+minutes.toString();
    }
    if(hours < 10){
        displayHours = "0"+hours.toString();
    }
    else{
        displayHours = hours;
    }

    document.getElementById("displayTimer").innerHTML = displayHours + ":" + displayMinutes + ":" + displaySeconds;
}


function startStop(){
    console.log("Clicked");
    console.log(status);
    if(status == "stopped"){
        console.log("Yep");
        var timer = document.getElementById("timerContent");
        timer.style.maxHeight = "200px";
        interval = window.setInterval(stopWatch, 10);
        document.getElementById("startStop").innerHTML = "Stop";
        status = "started";
    }
    else{
        window.clearInterval(interval);
        document.getElementById("startStop").innerHTML = "Start";
        status = "stopped";
    }
}

function reset()
{
    var timer = document.getElementById("timerContent");
    timer.style.maxHeight = "0px";
    window.clearInterval(interval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    status = "stopped";
    document.getElementById("startStop").innerHTML = "Start";
    document.getElementById("displayTimer").innerHTML = "00:00:00";
}

function stopTimer(){
    var select = document.getElementById('breakFreq');
    var value = select.options[select.selectedIndex].value;
    timeFreq = value;
    console.log("Value Changed!");
    console.log(breakFlag);

}
//////////////////////////////////////////

//Enable/Disable buttons
document.getElementById("mySwitch").addEventListener('change', function() {
    allBtns = document.querySelectorAll("button");
    if (this.checked) {
      console.log("Checkbox is checked..");
      console.log(allBtns);
      for(let b=0; b < allBtns.length; b++){
        console.log(allBtns[b].disabled);
        allBtns[b].disabled = false;
      }
    } 
    else {
      console.log("Checkbox is not checked..");
      console.log(allBtns);
      for(let b=0; b < allBtns.length; b++){
        console.log(allBtns[b].disabled);
        allBtns[b].disabled = true;
      }
    }
});
///////////////////////    

//Calling Server 

function loadPython() {
    console.log("Sending request for feed")
    const xhttp = new XMLHttpRequest();

    
    var img = document.getElementById( "bg" );  
    //img.src = "http://127.0.0.1:5000/cali_feed";
    img.src= 'http://localhost:5000/video_feed?area=41616&x=225&y=116&x1=429&y1=320'

/*    xhttp.open("GET", "http://127.0.0.1:5000/video_feed");
    xhttp.onreadystatechange = function() {
        console.log("helllloooo is there any respone",this.readyState,this.status);
        if (this.readyState == 3 && this.status == 200) {
            // var arrayBufferView = new Uint8Array( this.response );
            // var blob = new Blob( [ arrayBufferView ], { type: "image/jpeg" } );
            // var urlCreator = window.URL || window.webkitURL;
            // var imageUrl = urlCreator.createObjectURL( blob );
            //console.log("Image url is ",imageUrl);
            var img = document.getElementById( "bg" );  
            img.src = "http://127.0.0.1:5000/video_feed";
        }
     };
     xhttp.send();*/
  }





//Event Listeners:

document.getElementById("toggleCam").addEventListener("click", togglePreview);

document.getElementById("startStop").addEventListener("click", startStop);

document.getElementById("reset").addEventListener("click", reset);

document.getElementById("breakFreq").addEventListener("change", stopTimer);
