function hide_addr() {
  document.getElementById("addr").className = "hide";
  document.getElementById("loc").className = "";
}

function hide_loc() {
  document.getElementById("addr").className = "";
  document.getElementById("loc").className = "hide";
}

function initMap() {
  var directionsDisplay = new google.maps.DirectionsRenderer();
  var chicago = new google.maps.LatLng(41.850033, -87.6500523);
  var mapOptions = {
    zoom: 7,
    center: chicago
  };
  var map = new google.maps.Map(document.getElementById("map"), mapOptions);
  directionsDisplay.setMap(map);
}
