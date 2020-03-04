var x = document.getElementById("mapholder");

// function getLocation() {
//   if (navigator.geolocation) {
//     navigator.geolocation.watchPosition(showPosition);
//   } else {
//     x.innerHTML = "Geolocation is not supported by this browser.";
//   }
// }

function showPosition(lat,long) {
  var latlon = lat + "," + long;

  var img_url = "https://maps.googleapis.com/maps/api/staticmap?center="+latlon+"&size=400x300&markers=color:red%7Clabel:S%7C"+lat+","+long+"&key=AIzaSyBeUnLveEXl8MY27GnXVACU-gnhaGIMIQ8";

  document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
}
