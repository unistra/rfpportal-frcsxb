$( document ).ready(function() {

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
   var id = getUrlParameter('u');
   var redirect = getUrlParameter('redirect');

   console.log(redirect);

   $('#id_rfp').val(rfp);
   $('#id_user').val(id);


   if (redirect != 'undefined') {
       $('#redirect').attr('value', redirect);
   }

   $('#id_ending_date').datepicker();
   $('#id_starting_date').datepicker();



   $('html').bind('keypress', function(e)
        {
            if(e.keyCode == 13)
            {
                return false;
            }
        });
});