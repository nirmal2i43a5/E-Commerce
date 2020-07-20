

$(document).ready(function(){


    $("#js-search-form").on("click", function(event){
        event.preventDefault();
        var form = $(this);
  
            $.ajax({
                url: form.attr("action"),
                type: 'get',
                
            //   data: {'value_placeholder':searchWord},
                data : form.serialize(),
                dataType: 'json',
                success: function(data){
  
                    $("#get_table_body").html('');
                    $("#get_table_body").html(data['html_list']);
  
                },
               
  
            });

            
  
  
       
    });
  
  
  
  });