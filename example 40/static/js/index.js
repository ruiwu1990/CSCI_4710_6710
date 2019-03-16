$(document).ready(function(){
	$('#random_button').click(function(){
		// it won't wait this complex one finishes
		// the second get request will be done first
		$.get( "/api/random_number_complex", function( data ) {
	
		  console.log("Complex random number api");
		});
		$.get( "/api/random_number", function( data ) {
		  // you need to parse the required data first
		  data_json = JSON.parse(data);
		  $( "#random_num_p" ).text( data_json['number'] );
		  console.log("random number api");
		});

		// // place the second get request inside the first one
		// // then these two get requests will be executed in order
		// $.get( "/api/random_number_complex", function( data ) {
	
		//   console.log("Complex random number api");
		//   $.get( "/api/random_number", function( data ) {
		// 	  // you need to parse the required data first
		// 	  data_json = JSON.parse(data);
		// 	  $( "#random_num_p" ).text( data_json['number'] );
		// 	  console.log("random number api");
		// 	});
		// });
		
	});
});