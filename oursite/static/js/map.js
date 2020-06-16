function initMap() {
	var mapOptions = {
		zoom: 10,
		center: new google.maps.LatLng(2.970603, 30.920449),
		mapTypeId: 'roadmap'
    };
    
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);

	var goldenGatePosition = {lat: 2.970603,lng: 30.920449};
	var marker = new google.maps.Marker({
			position: goldenGatePosition,
			map: map,
			title: 'Amobit technologies'
			});

}
