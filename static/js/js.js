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
   var anchor =  getUrlParameter('a');
   var r = getUrlParameter('r');

   var block = getUrlParameter('block');

   var id_block = '#' + block;
   console.log('block');


   if (block != 'undefined'){
       $(id_block).removeClass('hide');
   }

   console.log(r);

   $('#id_rfp').val(rfp);
   $('#id_user').val(id);

   if (redirect != 'undefined') {
       $('#redirect').attr('value', redirect);
   }


   $('#id_ending_date').datepicker();
   $('#id_starting_date').datepicker();
   $('#id_deadline').datepicker();


   if (typeof anchor !== 'undefined'){
      $(document).scrollTop( $(anchor).offset() );
   };
});