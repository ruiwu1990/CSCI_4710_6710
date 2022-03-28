$(document).ready(function(){
	$('#display_button').click(function(){
		$.get( "/api/get_user", function( data ) {
		  // based on https://www.codebyamir.com/blog/populate-a-select-dropdown-list-with-json
		  var dropdown = $('#sel1');

		  dropdown.empty();
		  dropdown.append('<option selected="true" disabled>Choose a User</option>');
		  // .prop is used to change a property or an attribute of a HTML element
		  // selectedIndex is used to show which option is selected
		  dropdown.prop('selectedIndex', 0);

		  js_obj = JSON.parse(data);
		  total_len = js_obj['all_user'].length;
		  // TODO use for loop to fill the select list
		  
		  
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