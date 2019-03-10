$(document).ready(function(){
	$('#random_button').click(function(){
		$.get( "/api/random_number", function( data ) {
		  // you need to parse the required data first
		  data_json = JSON.parse(data);
		  $( "#random_num_p" ).text( data_json['number'] );
		});
	});
});