

function initMap() {
    var pos;
    var mapDiv = document.getElementById('map');
    var bounds = new google.maps.LatLngBounds();

    //temp array of locations - REPLACE WITH JSON DATA FROM Postgres
    var locations = [
        ['Transamerica Redwood Park', 37.795494, -122.402185],
        ['Transamerica Pyramid Center', 37.795335, -122.401836],
        ['3 Empire Park', 37.794511, -122.403843],
        ['Embarcadero Center West', 37.795183, -122.397395],
        ['California Street Plaza', 37.793005, -122.405228],
        ['Coworking Space', 37.793150, -122.404890],
        ['California Street Plaza 2', 37.792240, -122.403705],
        ['California Center Building', 37.792661, -122.400274],
        ['Charles Schwab Building', 37.793830, -122.399030],
        ['Garden Terrace', 37.793840, -122.398637],
        ['Pine Center', 37.792616, -122.398759],
        ['Fifty California Building', 37.794302, -122.397360],
        ['One California Building', 37.793511, -122.397140],
        ['Building and Plaza', 37.792990, -122.397870],
        ['', 37.791635, -122.398805],
        ['', 37.791208, -122.399951],
        ['Citigroup Center Atrium', 37.790723, -122.401112],
        ['Trinity Alley', 37.790306, -122.402583],
        ['Crocker Galleria', 37.789738, -122.403019],
        ['McKesson Plaza', 37.788970, -122.402687],
        ['Market Street', 37.789419, -122.400768],
        ['', 37.789860, -122.400345]
    ];

    //find user's location via geolocation and drop a marker
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            infoWindow.setPosition(pos);
            map.setCenter(pos);

            //sets user's current location marker on the map
            var userlocation = new google.maps.Marker({
                position: pos,
                map: map,
                title: 'You are Here!'
            });

            infoWindow.setContent('You are Here!'); //additional block, can replace with other color marker if we have time
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // if browser doesn't support Geolocation, throw an error.
        handleLocationError(false, infoWindow, map.getCenter());
    }
    //create map centered on users location
    var map = new google.maps.Map(mapDiv, {
        center: pos,
        zoom: 12,
        //styling for custom google map
        styles: [{
            featureType: 'all',
            stylers: [{
                saturation: -80
            }]
        }, {
            featureType: 'road.arterial',
            elementType: 'geometry',
            stylers: [{
                hue: '#00ffee'
            }, {
                saturation: 50
            }]
        }, {
            featureType: 'poi.business',
            elementType: 'labels',
            stylers: [{
                visibility: 'off'
            }]
        }, {
            featureType: 'water',
            elementType: 'geometry.fill',
            stylers: [{
                visibility: 'on'
            }, {
                hue: '#00eeff'
            }, {
                saturation: 40
            }]
        }, {
            featureType: 'landscape.natural',
            elementType: 'geometry.fill',
            stylers: [{
                visibility: 'on'
            }, {
                hue: '#00ff80'
            }, {
                saturation: 60
            }]
        }, {
            featureType: 'poi.park',
            elementType: 'geometry.fill',
            stylers: [{
                visibility: 'on'
            }, {
                hue: '#8CCBD0'
            }, {
                saturation: 60
            }]
        }]
    });

    var infoWindow = new google.maps.InfoWindow({
        map: map
    });
    //drop all location markers from array
    //for each location, extract the lat and long loop through the JSON data to create an annotation
    for (var i = 0; i < locations.length; i++) {
        createMarker(i);
    } //end for loop for place marker addition

    //call this separately to prevent last marker from always pulling up its content box on click
    function createMarker(i) {
        var marker;
        var position = new google.maps.LatLng(locations[i][1], locations[i][2]);

        bounds.extend(position);

        var contentString = '<div id="content">' + locations[i][0]
        '<p>Content goes here</p>' +
        '</div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });

        marker = new google.maps.Marker({
            position: position,
            map: map,
            title: 'hi!!',
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 5,
                strokeColor: '#277582'
            },
        });

        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map, marker);
        });
    }
    map.fitBounds(bounds);
} //end init map
