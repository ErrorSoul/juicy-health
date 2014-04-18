 $(document).ready(function(){
     var flag = false;
       $(window).bind('scroll', function() {
       
       var navHeight =  78;
	   
	   
             if ($(window).scrollTop() > navHeight) {
		 if (flag==false) {
		     
			 $('.navbar').fadeTo(0, 0.7);
			 $('.navbar').addClass('navbar-fixed-top');
			 flag=true;
		 }
		
             }
             else {
		 $('.navbar').removeClass('navbar-fixed-top');
		 $('.navbar').fadeTo(0, 1);
		 flag = false;
             }
        });
    });
