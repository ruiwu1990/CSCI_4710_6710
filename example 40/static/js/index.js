$(document).ready(function(){
	$('#display_button').click(function(){
		$.get( "/api/interact_user_table", function( data ) {
		  $('#result_id').text(data);
		});
	});
	$('#delete_button').click(function(){
		$.ajax({
			url: '/api/interact_user_table',
			type: 'DELETE_ALL',
			success: function(log){
				console.log(log);
			}
		});
	});
});