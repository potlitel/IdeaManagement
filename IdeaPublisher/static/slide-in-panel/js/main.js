jQuery(document).ready(function($){

	$('.cd-btn-right').on('click', function(event){
		var selectedItemId = $(this).attr("id");

		$.ajax({
            url : "searchPub/", // the endpoint
            type : "POST", // http method
            data : { id : selectedItemId}, // data sent with the delete request
            success : function(json_response) 
            {
              //document.getElementById("contentarea").setAttribute('data', '/feedback/details.html');
              event.preventDefault();
			        $('#right').addClass('is-visible');
			        console.log(json_response);
			      for (var i in json_response) 
              {
              	//console.log(json_response);
              	$('#title').html(json_response[i].fields.url);
              	$('#text').html(json_response[i].fields.text);
              }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
            }
        });
	});
	
	
	$('.searchCrzIdea').on('click', function(event){
		var selectedItemId = $(this).attr("id");

		$.ajax({
            url : "searchCrzIdea/", // the endpoint
            type : "POST", // http method
            data : { id : selectedItemId , object: "{{ object }}"}, // data sent with the delete request
            success : function(json_response) 
            {
              event.preventDefault();
			        $('#right').addClass('is-visible');
			        console.log(json_response);
			      for (var i in json_response) 
				  {
					$('#title').html(json_response[i].fields.titulo);
					var project = json_response[i].fields.project;

					if(project)	
					{
						$('#text').html("Description: " + json_response[i].fields.descripcion + "</br> Project: " + json_response[i].fields.project );
					}
					else
					{
						//alert(project);
						$('#text').html("Description: " + json_response[i].fields.descripcion);
					}
                  }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
            }
        });
	});
	
	
	//clode the lateral panel
	$('#right').on('click', function(event){
		if( $(event.target).is('#right') || $(event.target).is('.cd-panel-close') ) { 
			$('#right').removeClass('is-visible');
			event.preventDefault();
		}
	});
});