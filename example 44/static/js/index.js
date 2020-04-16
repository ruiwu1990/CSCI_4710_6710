$(document).ready(function(){
	$('#display_button').click(function(){
		$.get( "/api/get_team", function( data ) {
		  // clean display paragraph
		  $('#display_p').text('');
		  var js_obj = JSON.parse(data);

		  $.each(js_obj['all_teams'], function (index, entry) {
		  	// console.log(index);
		  	$('#display_p').append($("<span style='white-space: pre-line'></span><br>").text(entry.team_name)); 
		  });
		 
		});
	});
	$('#schedule_button').click(function(){

		$.get( "/api/generate_presentation_order", function( data ) {
		  // clean display paragraph
		  $('#display_p').text('');

		  var js_obj = JSON.parse(data);
		  $('#display_p').append($("<span style='white-space: pre-line'></span><br>").text('Fist Day:'));
		  $.each(js_obj['first_day'], function (index, entry) {
		  	// console.log(index);
		  	$('#display_p').append($("<span style='white-space: pre-line'></span><br>").text(entry.team.team_name+', '+entry.start_time));
		    
		  });

		  $('#display_p').append($("<span style='white-space: pre-line'></span><br>").text('Second Day:'));
		  $.each(js_obj['second_day'], function (index, entry) {
		  	// console.log(index);
		  	$('#display_p').append($("<span style='white-space: pre-line'></span><br>").text(entry.team.team_name+', '+entry.start_time));
		    
		  });
		});
	});
});