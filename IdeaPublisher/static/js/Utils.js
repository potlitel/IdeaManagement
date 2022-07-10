;(function(Utils) {
  'use strict';

Utils.testingAjax = function(valueSearch)
{
    $.ajax({
            url : "searchPub/", // the endpoint
            type : "POST", // http method
            data : { id : valueSearch }, // data sent with the delete request
            success : function(json_response) 
            {
              console.log(json_response);
              // Ocultamos el div "indicador"
     //          $('#loading').hide();
     //          // Visualizamos el div que muestra los resultados de la búsqueda
     //          $('#searchResults').show();

     //          if (json_response.length == 0) {
     //                $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda no ha retornado ningún resultado para el criterio especificado</div>");
     //          }else
     //          {
     //             // Visualizamos el div que muestra los resultados de la búsqueda
				 // $('#searchResultsBody').show();
     //             if (json_response.length==1) 
     //             {
     //                $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultado para el criterio especificado</div>");
     //             }else
     //             {
     //                $('#searchResults').html("<div><img src='../../static/img/ic_search_48px-128.png' width=25px height=25px/>La búsqueda ha retornado "+ json_response.length +" resultados para el criterio especificado</div>");
     //             }
     //             for (var i in json_response) 
     //              {
					// $('#searchResultsBody').append("<a href='PublicacionView/" + json_response[i].pk + "'>" + json_response[i].fields.titulo + "</a>, del autor "+ json_response[i].fields.autor +" publicada en el año "+ json_response[i].fields.anno +"</br>");
     //              }   
     //          }
            },
            error : function(xhr,errmsg,err) {
                // Show an error
            //     $('#searchResults').html("<div class='alert-box alert radius' data-alert>"+
            //     "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
            //     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });

}    

})(window.Utils = window.Utils || {});