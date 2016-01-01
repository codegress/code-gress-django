$(document).ready(function(){
    $(".handle-tooltip").tooltip({title: "Profile and more"});
    
    $('#signup-btn').click(function(event){
    	event.preventDefault();
    	var invalid =false;
    	if(!$('#handle').val()){
    		$('#handle-group').addClass('has-warning has-feedback');
			$('#handle-feedback').addClass('glyphicon-warning-sign');
			$('#handle-feedback').removeClass('hide');		
			invalid =true;
    	}
    	if(!$('#email').val()){
    		$('#email-group').addClass('has-warning has-feedback');
			$('#email-feedback').addClass('glyphicon-warning-sign');	
			$('#email-feedback').removeClass('hide');
			invalid =true;
    	}
    	if(!$('#password').val()){
    		$('#password-group').addClass('has-warning has-feedback');
			$('#password-feedback').addClass('glyphicon-warning-sign');	
			$('#password-feedback').removeClass('hide');
			invalid =true;
    	}
    	else{
    		
    	}
		if(!invalid){
			$('#signup-form').submit();
		}
    });

    //CSRF TOKEN FOR POST METHODS
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}
	
	function csrfSafeMethod(method) {
 	   // these HTTP methods do not require CSRF protection
    	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

    function sendAjaxPost(data_to_send,url,success_func){
    	$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		        }
		    }
		});
    	$.ajax({
    		url:url,
    		method:'POST',
    		data:data_to_send,
    		success:success_func
    	});
    }

    $('#handle').on({
    	keyup:function(){
	    	if($(this).val().trim()){
	    		request = {'handle':$(this).val()}
	    		sendAjaxPost(request,'/signup/check/handle',handleAjaxSuccess);
	    	}
    	},
    	blur:function(){
    		if(!$(this).val().trim()){
    			$('#handle-group').addClass('has-warning has-feedback');
				$('#handle-feedback').addClass('glyphicon-warning-sign');	
				$('#handle-feedback').removeClass('hide');
    		}
    	}
    });
    
    function handleAjaxSuccess(response){
		if(!response['handle_registered'] && response['handle_valid']){
			$('#handle-group').removeClass('has-warning has-feedback');
			$('#handle-feedback').removeClass('glyphicon-warning-sign');
			$('#handle-group').addClass('has-success has-feedback');
			$('#handle-feedback').addClass('glyphicon-ok');
			$('#handle-feedback').removeClass('hide');
		}
		else{
			$('#handle-group').removeClass('has-success has-feedback');
			$('#handle-feedback').removeClass('glyphicon-ok');
			$('#handle-group').addClass('has-warning has-feedback');
			$('#handle-feedback').addClass('glyphicon-warning-sign');
			$('#handle-feedback').removeClass('hide');
		}
	}

	function emailAjaxSuccess(response){
		if(response['email_valid'] && !response['email_registered']){
			$('#email-group').removeClass('has-warning has-feedback');
			$('#email-feedback').removeClass('glyphicon-warning-sign');
			$('#email-group').addClass('has-success has-feedback');
			$('#email-feedback').addClass('glyphicon-ok');
			$('#email-feedback').removeClass('hide');
		}
		else{
			$('#email-group').removeClass('has-success has-feedback');
			$('#email-feedback').removeClass('glyphicon-ok');
			$('#email-group').addClass('has-warning has-feedback');
			$('#email-feedback').addClass('glyphicon-warning-sign');	
			$('#email-feedback').removeClass('hide');
		}
	};

	$('#email').on({
		blur:function(){
    		if(!$(this).val().trim()){
    			$('#email-group').addClass('has-warning has-feedback');
				$('#email-feedback').addClass('glyphicon-warning-sign');	
				$('#email-feedback').removeClass('hide');
    		}
    		else{
    			request = {'email':$(this).val()}
	    		sendAjaxPost(request,'/signup/check/email',emailAjaxSuccess);
    		}
    	}
	});
});