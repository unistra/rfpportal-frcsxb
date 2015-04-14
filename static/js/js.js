$( document ).ready(function() {

   console.log( "Script initiated!" );

  //  $('.edit').hide();
   // $('#save').hide();
   // $('#project-name').hide();

   //$('#edit').click(function(){
     //       $(this).slideUp(500);
       //     $('#save').slideDown(500);
         //   $('.edit').slideDown(500);
          //  $('.project_data').slideUp(500);
   //});

    function getUrlParameter(sParam)
    {
        var sPageURL = window.location.search.substring(1);
        var sURLVariables = sPageURL.split('&');
        for (var i = 0; i < sURLVariables.length; i++)
        {
            var sParameterName = sURLVariables[i].split('=');
            if (sParameterName[0] == sParam)
            {
                return sParameterName[1];
            }
        }
    }

   var rfp = getUrlParameter('rfp');
   $('#id_rfp_id').val(rfp);
   console.log(rfp);

});