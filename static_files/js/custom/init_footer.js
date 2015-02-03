	 $(document).ready(function() {
       
	    $('#id_rooms').select2();
	    $('#id_type').select2();
	    $('#id_category').select2();
	    $('#id_borough').select2();
	    $('#id_neighborhood').select2();
	    $('#id_subject').select2();


            $('#id_message').on('change',function() {
                    $('#sms-failure-message').fadeOut( "slow" );
                    $('#sms-success-message').fadeOut( "slow" );
            });



	    $('#id_subject').on('change',function() {
		    $('#failure-message').fadeOut( "slow" );
		    $('#success-message').fadeOut( "slow" );
	    });

	    $('#id_name').on('change',function() {
		    $('#failure-message').fadeOut( "slow" );
		    $('#success-message').fadeOut( "slow" );
	    });

	    $('#id_email').on('change',function() {
		    $('#failure-message').fadeOut( "slow" );
		    $('#success-message').fadeOut( "slow" );
	    });

	    $('#id_message').on('change',function() {
		    $('#failure-message').fadeOut( "slow" );
		    $('#success-message').fadeOut( "slow" );
	    });
	     
	    $('#contact-submit').on('mouseout',function() {
		    $('#success-message').fadeOut( "slow" ); 
		    $('#contact-valid').attr('value','true');                    
	     });
	     $('#id_message').on('mouseout',function() {
		    $('#success-message').fadeOut( "fast" );
	     });
	     $('#id_name').on('mouseout',function() {
		    $('#success-message').fadeOut( "fast" );
	     });
	     $('#id_email').on('mouseout',function() {
		    $('#success-message').fadeOut( "fast" );
	     });
	     $('#id_subject').on('mouseout',function() {
		    $('#success-message').fadeOut( "fast" );
	     });


	    $('#contact-submit').on('click',function() {
		if  ($('#contact-valid').val() == 'true') {         
		    $('#failure-message').fadeIn( "fast" );
		}
		if  ($('#contact-valid').val() == 'false') {
		    $('#failure-message').fadeOut( "fast" );
		    $('#success-message').fadeIn( "slow" );
		}

	    });
	    


	    $('#bnt_search').bind('click',function() {
	//             $("form[name='property_form']").submit();
	    }); 
	    $('#contact-us').mouseover(function(){
		     $('#contact-us img').attr('src','http://zrealtycorp.com/media/images/contact_us_button_on.png');
	     });
	    $('#contact-us').mouseout(function() {
		     $('#contact-us img').attr('src','http://zrealtycorp.com/media/images/contact_us_button_off.png');
	     });
	    $('#send').mouseover(function(){
		     $('#send img').attr('src','http://zrealtycorp.com/media/images/send_off.png');
	     });
	    $('#send').mouseout(function() {
		     $('#send img').attr('src','http://zrealtycorp.com/media/images/send_on.png');
	     });

	    $('#contact-us').bind('click',function() {
		$('#contact-form').css('display','block');

	     });
	    $("#message").autosize();
	    $("#contact-form").draggable();
	    $("#contact-form").resizable();
	    $('#contact-form').css('display','none');

            $("#comment-form").draggable();
            $("#comment-form").resizable();
            $('#comment-form').css('display','none');

            $("#add-comment-blog").bind('click', function() {
                 $('#comment-form').css('display','block');
             });

	    $('#is_search_open').attr('value','false');
	    $("#search_header").css('display','none');
	    $('#is_properties_open').attr('value','false');

	    $('#search-area').css('display','none');
	    $('#properties-area').css('display','none');

             var currentMousePos = { x: -1, y: -1 };
            $(document).mousemove(function(event) {
                   currentMousePos.x = event.pageX;
                   currentMousePos.y = event.pageY;
             });


	    $('div#home a').on('mouseover',function() {
                  $('#submenu-wrapper-1').css('display','block');
                  $('#submenu-wrapper-2').css('display','none');
                  $('#submenu-wrapper-3').css('display','none');   
                  
                  if  (currentMousePos.x>=1419) {
                      $('#submenu-wrapper-1').css('margin-left','59.7%'); 
                  }

                  if  (currentMousePos.x>=1279 && currentMousePos.x<=1330) {
                      $('#submenu-wrapper-1').css('margin-left','58.2%');
                  }
                  if  (currentMousePos.x >= 1138 && currentMousePos.x <= 1198) {
                      $('#submenu-wrapper-1').css('margin-left','56.4%');
                  }
                  if  (currentMousePos.x>=997 && currentMousePos.x<=1057) {
                      $('#submenu-wrapper-1').css('margin-left','54.0%');
                  }

                  if  (currentMousePos.x>=855 && currentMousePos.x<=906) {
                      $('#submenu-wrapper-1').css('margin-left','51.2%');
                  }
 
                  if  (currentMousePos.x>=713 && currentMousePos.x<=765) {
                      $('#submenu-wrapper-1').css('margin-left','47.5%');
                  }

                  if  (currentMousePos.x>=573 && currentMousePos.x<=624) {
                      $('#submenu-wrapper-1').css('margin-left','42.9%');
                  }


                  if  (currentMousePos.x>=443 && currentMousePos.x<=490) {
                      $('#submenu-wrapper-1').css('margin-left','37.1%');
                  }

                  if  (currentMousePos.x>=356 && currentMousePos.x<=394) {
                      $('#submenu-wrapper-1').css('margin-left','31.9%');
                  }


	     });
             $('#about a').on('mouseover',function() {
                  if  (currentMousePos.x>=1473) {
                      $('#submenu-wrapper-2').css('margin-left','62.5%');
                  }
                  if  (currentMousePos.x>=1333 && currentMousePos.x<=1394) {
                      $('#submenu-wrapper-2').css('margin-left','61.2%');
                  }
                  if  (currentMousePos.x>=1191 && currentMousePos.x<=1242) {
                      $('#submenu-wrapper-2').css('margin-left','59.5%');
                  }
                  if  (currentMousePos.x>=1050 && currentMousePos.x<=1100) {
                      $('#submenu-wrapper-2').css('margin-left','57.8%');
                  }

                  if  (currentMousePos.x>=909 && currentMousePos.x<=959) {
                      $('#submenu-wrapper-2').css('margin-left','51.2%');
                  }

                  if  (currentMousePos.x>=768 && currentMousePos.x<=818) {
                      $('#submenu-wrapper-2').css('margin-left','52.1%');
                  }

                  if  (currentMousePos.x>=627 && currentMousePos.x<=677) {
                      $('#submenu-wrapper-2').css('margin-left','48.2%');
                  }


                  if  (currentMousePos.x>=494 && currentMousePos.x<=544) {
                      $('#submenu-wrapper-2').css('margin-left','43.6%');
                  }


                  if  (currentMousePos.x>=395 && currentMousePos.x<=445) {
                      $('#submenu-wrapper-2').css('margin-left','38.3%');
                  }

                  $('#submenu-wrapper-1').css('display','none');
                  $('#submenu-wrapper-2').css('display','block');
                  $('#submenu-wrapper-3').css('display','none');
             });


             $('#blog a').on('mouseover',function() {
                  if  (currentMousePos.x>=1522) {
                      $('#submenu-wrapper-3').css('margin-left','65.3%');
                  }

                  if  (currentMousePos.x>=1385 && currentMousePos.x<=1435) {
                      $('#submenu-wrapper-3').css('margin-left','64.5%');
                  }
                  if  (currentMousePos.x>=1244 && currentMousePos.x<=1294) {
                        $('#submenu-wrapper-3').css('margin-left','63.0%');
                  }

                  if  (currentMousePos.x>=1105 && currentMousePos.x<=1154) {
                      $('#submenu-wrapper-3').css('margin-left','61.2%');
                  }

                  if  (currentMousePos.x>=962 && currentMousePos.x<=1113) {
                      $('#submenu-wrapper-3').css('margin-left','61.2%');
                  }

                  if  (currentMousePos.x>=821 && currentMousePos.x<=871) {
                      $('#submenu-wrapper-3').css('margin-left','57.2%');
                  }

                  if  (currentMousePos.x>=680 && currentMousePos.x<=731) {
                      $('#submenu-wrapper-3').css('margin-left','53.9%');
                  }


                  if  (currentMousePos.x>=545 && currentMousePos.x<=595) {
                      $('#submenu-wrapper-3').css('margin-left','50.1%');
                  }

                  if  (currentMousePos.x>=434 && currentMousePos.x<=472) {
                      $('#submenu-wrapper-3').css('margin-left','44.5%');
                  }

                  $('#submenu-wrapper-1').css('display','none');
                  $('#submenu-wrapper-2').css('display','none');
                  
                  $('#submenu-wrapper-3').css('display','block');
             });

	    $('#about a').on('mouseover',function() {
		  $('#submenu-wrapper-1').css('display','none');
	     });
	     $('#submenu-wrapper-1 ul').on('mouseover',function() {
		 $('#submenu-wrapper-1').css('display','block');
	     });
	     $('#submenu-wrapper-1 .header').on('mouseover',function() {
		 $('#submenu-wrapper-1').css('display','block');
	     });
	     $('#submenu-wrapper-1 .footer').on('mouseover',function() {
		 $('#submenu-wrapper-1').css('display','block');
	     });
            $('#submenu-wrapper-1').on('mouseout',function() { 
                 $('#submenu-wrapper-1').css('display','none');
             });






            $('#about a').on('mouseover',function() {
                  $('#submenu-wrapper-2').css('display','block');
                  $('#submenu-wrapper-1').css('display','none');
                  $('#submenu-wrapper-3').css('display','none');
             });

            $('#home a').on('mouseover',function() {
                  $('#submenu-wrapper-1').css('display','block');
                  $('#submenu-wrapper-2').css('display','none');
                  $('#submenu-wrapper-3').css('display','none');
             });

            $('#blog a').on('mouseover',function() {
                  $('#submenu-wrapper-3').css('display','block');
                  $('#submenu-wrapper-2').css('display','none');
                  $('#submenu-wrapper-1').css('display','none');
             });

             $('#submenu-wrapper-2 ul').on('mouseover',function() {
                 $('#submenu-wrapper-2').css('display','block');
             });
             $('#submenu-wrapper-2 .header').on('mouseover',function() {
                 $('#submenu-wrapper-2').css('display','block');
             });
             $('#submenu-wrapper-2 .footer').on('mouseover',function() {
                 $('#submenu-wrapper-2').css('display','block');
             });
            $('#submenu-wrapper-2').on('mouseout',function() {
                 $('#submenu-wrapper-2').css('display','none');
             });

             
        

            $('#search a').on('mouseover',function() {
                  $('#submenu-wrapper-3').css('display','none');
                  
             });

             $('#submenu-wrapper-3 ul').on('mouseover',function() {
                 $('#submenu-wrapper-3').css('display','block');
             });
             $('#submenu-wrapper-3 .header').on('mouseover',function() {
                 $('#submenu-wrapper-3').css('display','block');
             });
             $('#submenu-wrapper-3 .footer').on('mouseover',function() {
                 $('#submenu-wrapper-3').css('display','block');
             });
            $('#submenu-wrapper-3').on('mouseout',function() {
                 $('#submenu-wrapper-3').css('display','none');
             });
              
             

                

  });
