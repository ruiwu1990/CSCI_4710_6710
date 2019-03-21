$(document).ready(function(){
	$('#display_button').click(function(){
		$.get( "/api/get_user", function( data ) {
		  var dropdown = $('#sel1');

		  // TODO!!!!!
		});
	});
	$('#delete_button').click(function(){
		$.ajax({
			url: '/api/delete_user/'+$('#sel1').find(":selected").text(),
			type: 'MY_DELETE',
			success: function(log){
				console.log(log);
			}
		});
	});
});