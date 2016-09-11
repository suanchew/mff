
function initMap() {
    var pos;
    var mapDiv = document.getElementById('map');
    var bounds = new google.maps.LatLngBounds();

    //temp array of locations - REPLACE WITH JSON DATA FROM Postgres
    var locations = [
        ['3 Empire Park', 37.794511, -122.403843]
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

        var contentString = '<div id="content">' + '<a href="/home">Empire Park Public Space</a>'
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
