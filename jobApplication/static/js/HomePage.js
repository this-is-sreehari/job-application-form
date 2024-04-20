// to create a close button for alert window
var alert_box = document.getElementById("alert-box");

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    alert_box.style.display = "none";
  }
