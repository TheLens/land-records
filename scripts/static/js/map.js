var map, dataLayer, neighborhoodLayer;
var clicked = 0;
var dropdownFocus = 0;//0 is standard. dropdown selection = 1

function updateMap(data, mapsearching, backforward) {
  tablesorterOptions();

  var center = map.getCenter();
  var zoom = map.getZoom();

  addDataToMap(data);

  if (mapsearching === 1) {
    // If box is checked yes, don't alter user's view 
    map.setView(center, zoom);
  } else if (mapsearching === 0) {
    if (backforward !== 1) {
      if (Object.keys(dataLayer._layers).length === 0) { //if there aren't any points on the map
        map.setView(center, zoom);
      } else {
        map.fitBounds(dataLayer.getBounds(), {padding: [5, 5]});
      }
    }
  }

  //tableHover(dataLayer);
  //mapHover(dataLayer);
}

function updateNeighborhoodLayer(data) {
  console.log('updateNeighborhoodLayer');
  console.log(data);

  if (map.hasLayer(neighborhoodLayer)) {
    map.removeLayer(neighborhoodLayer);
  }

  neighborhoodLayer = L.geoJson(data, {
    // filter: function (feature, layer) {
    //   if (feature.properties) {
    //     // If the property "underConstruction" exists and is true, return false (don't render features under construction)
    //     return feature.properties.underConstruction !== undefined ? !feature.properties.underConstruction : true;
    //   }
    //   return false;
    // },
    style: {
      fillColor: "white",
      fillOpacity: 0,
      color: "#B33125",
      opacity: 1,
      weight: 2,
      dashArray: "5, 5"
    }
    //onEachFeature: onEachFeature
  }).addTo(map);
  
  map.fitBounds(neighborhoodLayer);
}

function selectedNeighborhood(neighborhood) {
  console.log('neighborhood:', neighborhood);
  neighborhood = decodeURIComponent(neighborhood).toUpperCase();
  console.log('neighborhood:', neighborhood);
  neighborhood = neighborhood.replace(/ /g, '+');

  console.log('neighborhood:', neighborhood);

  var url = "http://localhost:5000/static/neighborhood-geojson/" + neighborhood + ".js";
  var static_url = '../../static/neighborhood-geojson/' + neighborhood + '.js';
  var s3_url = 'https://s3-us-west-2.amazonaws.com/lensnola/land-records/neighborhood-geojson/' + neighborhood + '.json';

  $.ajax({
    url: s3_url,
    type: "GET",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    success: function(data) {
      console.log('data:', data);
      testGeoJSON = data;
      console.log(testGeoJSON);

      updateNeighborhoodLayer(data);
    }
  });
}

function loadMapTiles() {
  var stamenLayer = new L.StamenTileLayer("toner-lite", {
    minZoom: 9,
    type: 'png',
    attribution: '<span id="attribution-text">Map data © <a href="http://openstreetmap.org" target="_blank">OpenStreetMap</a>. Tiles by <a href="http://stamen.com" target="_blank">Stamen Design</a>. <a href="http://sos.la.gov/">sos.la.gov</a></span>',
    scrollWheelZoom: false,
    detectRetina: true
  });

  L.mapbox.accessToken = 'pk.eyJ1IjoidHRob3JlbiIsImEiOiJEbnRCdmlrIn0.hX5nW5GQ-J4ayOS-3UQl5w';
  var mapboxLayer = L.tileLayer('https://{s}.tiles.mapbox.com/v3/tthoren.i7m70bek/{z}/{x}/{y}.png', {
    attribution: "<a href='https://www.mapbox.com/about/maps/' target='_blank'>&copy; Mapbox &copy; OpenStreetMap</a> <a class='mapbox-improve-map' href='https://www.mapbox.com/map-feedback/' target='_blank'>Feedback</a>",
    scrollWheelZoom: false,
    detectRetina: true,
    minZoom: 9
    //opacity: 0
  });
  var satelliteLayer = L.tileLayer('https://{s}.tiles.mapbox.com/v3/tthoren.i7m6noin/{z}/{x}/{y}.png', {
    attribution: "<a href='https://www.mapbox.com/about/maps/' target='_blank'>&copy; Mapbox &copy; OpenStreetMap</a> <a class='mapbox-improve-map' href='https://www.mapbox.com/map-feedback/' target='_blank'>Feedback</a>",
    scrollWheelZoom: false,
    detectRetina: true,
    minZoom: 9
  });

  var tileTimeout;

  function switchToStamen() {
    clearTimeout(tileTimeout);
    console.error('Not finding Stamen tiles. Switching to OSM tiles...');
    map.removeLayer(mapboxLayer);
    map.addLayer(stamenLayer);
  }

  var baseMaps = {
    "Color": mapboxLayer,
    "Satellite": satelliteLayer
  };

  map.addLayer(mapboxLayer);
  L.control.layers(baseMaps).addTo(map);

  tileTimeout = setTimeout(switchToStamen, 10000);

  mapboxLayer.on('tileload', function(e) {
    clearTimeout(tileTimeout);
  });
}

function addLensLogoToMap() {
  var logo = L.control({position: 'bottomleft'});
  logo.onAdd = function () {
    var div = L.DomUtil.create('div');
    div.innerHTML = "<img src='https://s3-us-west-2.amazonaws.com/lensnola/land-records/css/images/lens-logo-retina.png' alt='Lens logo' width='100'>";
    return div;
  };
  logo.addTo(map);
}

function createMap() {
  map = new L.Map("map", {
    minZoom: 9,
    maxZoom: 18,
    scrollWheelZoom: false,
    fadeAnimation: false,
    zoomControl: false
  });

  // Add zoom control to top left corner of the map.
  L.control.zoom({position: 'topleft'}).addTo(map);
}

function onEachFeature(feature, layer) {
  /*
  Leaflet functions to be assigned to each feature on a given layer.
  */
  layer.on({
    click: clickFeature,
    mouseover: highlightFeature,
    mouseout: resetHighlight
  });
}

function clickFeature(e) {
  /*
  Clicked on a feature, such as a precinct or parish.
  */

  instrument_no = e.target.feature.properties.instrument_no;
  //console.log('instrument_no:', instrument_no);
  window.location.href = "/realestate/sale/" + instrument_no;
}

function highlightFeature(e) {
  /*
  Hover on a feature, such as a precinct or parish.
  */

  var layer = e.target;
  var feature = e.target.feature;

  if (clicked === 1) {
    return;
  }
  var html;
  html = "<div class='popup'>" +
    "<strong>Date: </strong>" + feature.properties.document_date + "<br>" +
    "<strong>Amount: </strong>" + feature.properties.amount + "<br>" +
    "<strong>Address: </strong>" + (feature.properties.address).trunc(150) + "<br>" +
    "<strong>Location info: </strong>" + (feature.properties.location_info).trunc(150) + "<br>" +
    "<strong>Sellers: </strong>" + feature.properties.sellers + "<br>" +
    "<strong>Buyers: </strong>" + feature.properties.buyers + "<br>" +
    "<br><a><em>Click marker for more information.</em></a>" +
  "</div>";
  if (!L.Browser.ie && !L.Browser.opera) { // Fix for IE and Opera
    layer.bringToFront();
  }
  $('#tooltip').html(html);
  var tooltip_height = $('#tooltip').outerHeight(true);
  $('#tooltip').css({"display": "block",
    "left": (
      e.containerPoint.x < (map._size.x / 3) ?
        e.originalEvent.pageX :
        (e.containerPoint.x >= (map._size.x / 3) && e.containerPoint.x < (2 * map._size.x / 3) ?
          e.originalEvent.pageX - 235 / 2 :
          e.originalEvent.pageX - 235
        )
    ),
    "top": (
      e.containerPoint.y < (map._size.y / 2) ?
        e.originalEvent.pageY + 20 :
        e.originalEvent.pageY - tooltip_height - 20
    )
  });
}

function resetHighlight(e) {
  /*
  Clicked on a feature, such as a precinct or parish.
  */

  if (clicked === 1) {
    return;
  }
  $('#tooltip').css({"display": "none"});
}

function resetClicked() {
  /*
  Ensure tooltip's 'clicked' variable is equal to 0.
  */

  if (clicked === 1) {
    clicked = 0;
    resetHighlight();
  }
}

function addDataToMap(data) {
  var dataLayer2 = L.geoJson(data, {
    onEachFeature: onEachFeature,
    pointToLayer: function (feature, layer) {
      return L.circleMarker(layer, {
        radius: 10,
        color: 'white',
        opacity: 0.8,
        fillColor: '#B33125',
        fillOpacity: 0.5
      });
    }
  });

  if (map.hasLayer(dataLayer)) {
    map.removeLayer(dataLayer);
  }
  dataLayer = dataLayer2;
  map.addLayer(dataLayer);

  dataLayer.eachLayer(function (layer) {
    layer.on('mouseover', function (event) {
      layer.setStyle({radius: 10, color: 'white', opacity: 1.0, fillColor: '#B33125', fillOpacity: 1.0});
      layer.bringToFront();
    });
    layer.on('mouseout', function (event) {
      layer.setStyle({radius: 10, color: 'white', opacity: 0.8, fillColor: '#B33125', fillOpacity: 0.5});
    });
  });
}

function initialMapFunction(data) {
  // Not sure what this is
  tablesorterOptions();

  createMap();
  loadMapTiles();
  addLensLogoToMap();
  addDataToMap(data);

  if (Object.keys(dataLayer._layers).length === 0) { //if there aren't any points on the map
    map.setView([29.996953, -90.048277], 11);
  } else {
    map.fitBounds(dataLayer.getBounds(), {paddingTopLeft: [5, 5], paddingBottomRight: [5, 5]});
  }
  
  //tableHover(dataLayer);
  //mapHover(dataLayer);

  map.on('moveend', function (e) {
    if (document.getElementById("mapButton").checked === true) {
      mapSearching();
    }
  });
  map.on('click', function(e) {
    resetClicked();
  });
}

function mapHover(dataLayer) {
  dataLayer.eachLayer(function (layer) {
    layer.on('mouseover', function (event) {
      layer.setStyle({radius: 10, color: 'white', opacity: 1.0, fillColor: '#B33125', fillOpacity: 1.0});
      layer.bringToFront();
    });
    layer.on('mouseout', function (event) {
      layer.setStyle({radius: 10, color: 'white', opacity: 0.8, fillColor: '#B33125', fillOpacity: 0.5});
    });
  });
}

$(document).on('mouseenter', "#myTable tbody tr td", function (event) {
  var parent = $(event.target).parent().attr('id');
  dataLayer.eachLayer(function (layer) {
    if (layer.feature.properties.instrument_no === parent) {
      layer.setStyle({radius: 10, color: 'white', opacity: 1.0, fillColor: '#B33125', fillOpacity: 1.0});
      layer.bringToFront();
    }
    if (layer.feature.properties.instrument_no !== parent) {
      layer.setStyle({radius: 10, color: 'white', opacity: 1.0, fillColor: '#B33125', fillOpacity: 0.5});
    }
  });
});
$(document).on('mouseleave', "#myTable tbody tr td", function (event) {
  var parent = $(event.target).parent().attr('id');
  dataLayer.eachLayer(function (layer) {
    if (layer.feature.properties.instrument_no === parent) {
      layer.setStyle({radius: 10, color: 'white', opacity: 0.8, fillColor: '#B33125', fillOpacity: 0.5});
    }
    if (layer.feature.properties.instrument_no !== parent) {
      layer.setStyle({radius: 10, color: 'white', opacity: 0.8, fillColor: '#B33125', fillOpacity: 0.5});
    }
  });
});
