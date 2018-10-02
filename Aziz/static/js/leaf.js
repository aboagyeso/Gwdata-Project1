var defaultURL = "/leaf";
d3.json(defaultURL, function(response) {

  // Create a new marker cluster group
  var markers = L.markerClusterGroup({
    animateAddingMarkers: true
  });

  // Loop through data
  for (var i = 0; i < response.length; i++) {

    // Set the data location property to a variable
    //var location = response[i].location;

    // Check for location property
   // if (location) {

      // Add a new marker to the cluster group and bind a pop-up
    markers.addLayer(L.marker([x, y])
    .bindPopup(x, y));
    

  }

  // Add our marker cluster layer to the map
  myMap.addLayer(markers);

});
