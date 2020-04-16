$(document).ready(function(){

	$('#check_button_id').click(function(){
		var get_url = '/api/process_csv/' + $('#lower_id').val().toString() + '/' + $('#upper_id').val().toString();
		
		$.get( get_url, function( data ) {
		  data_obj = JSON.parse(data);
		  $('#result_p').text(JSON.stringify(data))
		  console.log(data_obj['Temperature']);
		});
		
	});
});

