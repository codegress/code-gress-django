$(document).ready(function(){
    $(".handle-tooltip").tooltip({title: "Profile and more"});
    $('#handle-feedback').css({display:'none'})
    $('#email-feedback').css({display:'none'})
    $('#password-feedback').css({display:'none'})

    $('#handle').blur(function(){
    	$('#handle-group').addClass('has-warning has-feedback');
		$('#handle-feedback').addClass('glyphicon-warning-sign');
		$('#handle-feedback').css({display:'block'});
    });
    
    $('#email').blur(function(){
    	$('#email-group').addClass('has-warning has-feedback');
    	$('#email-feedback').addClass('glyphicon-warning-sign');
		$('#email-feedback').css({display:'block'});
    });

    $('#password').blur(function(){
    	$('#password-group').addClass('has-warning has-feedback');
    	$('#password-feedback').addClass('glyphicon-warning-sign');
		$('#password-feedback').css({display:'block'});
    });
    
    $('#handle').keyup(function(){
    	request = {'handle':$(this).val()}
    	sendAjaxPost(request,'/signup/check/handle',handleAjaxSuccess);
    });
    function handleAjaxSuccess(response){
		if(response['handle_registered']){
			$('#handle-group').addClass('has-warning has-feedback');
			$('#handle-feedback').addClass('glyphicon-warning-sign');
			$('#handle-feedback').css({display:'block'});
		}
		else{
			$('#handle-group').removeClass('has-warning has-feedback');
			$('#handle-group').addClass('has-success has-feedback');
			$('#handle-feedback').removeClass('glyphicon-warning-sign');
			$('#handle-feedback').addClass('glyphicon-ok');
		}
	}
    function sendAjaxPost(data_to_send,url,func){
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
    		success:func
    	});
    }
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
});