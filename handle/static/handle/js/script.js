$(document).ready(function(){
    $(".handle-tooltip").tooltip({title: "Profile and more",placement:'bottom'});
    // $('#privacy-lock').tooltip();
    $('#privacy-lock').click(function(e){
        e.preventDefault();
        var lock = $(this).children('span');
        if(lock.hasClass('glyphicon-eye-close')){
            lock.removeClass('glyphicon-eye-close');
            lock.addClass('glyphicon-eye-open');
            $(this).attr({title:'Email Public'});
            // $(this).tooltip();
        }
        else{
            lock.removeClass('glyphicon-eye-open');
            lock.addClass('glyphicon-eye-close');
            $(this).attr({title:'Email Private'});   
            // $(this).tooltip();
        }
    });
    $('#signup-btn').click(function(e){
    	e.preventDefault();
        var form_groups = $('#signup-form').children('div');
        var validated = {}
        if(!validated['password']){
            current_password = {'password':$('#signup-form #password').val()};
            url_to_send = '/signup/check/pass';
            var success = function(data){
                if(data['valid']){
                    $('#password-group').removeClass('has-warning');
                    $('#password-feedback').removeClass('glyphicon-warning-sign');
                    $('#password-group').addClass('has-feedback has-success');
                    $('#password-feedback').addClass('glyphicon-ok');
                    $('#password-feedback').removeClass('hide');
                    validated['password'] = true;
                }
                else{
                    $('#password-group').removeClass('has-success');
                    $('#password-feedback').removeClass('glyphicon-ok');
                    $('#password-group').addClass('has-feedback has-warning');
                    $('#password-feedback').addClass('glyphicon-warning-sign');
                    $('#password-feedback').removeClass('hide');
                }
            };
            sendAjaxPost(current_password,url_to_send,success);
        }
        if(!hasEmptyFields(form_groups)){
            form_groups.each(function(){
                var feedback = $(this).find('span');
                if(feedback.hasClass('glyphicon-ok')){
                    var key = $(this).find('input')[0]['id'];
                    validated[key]=true;
                }
            });
            var length = Object.keys(validated).length;
            if(length == 3){
                $('#signup-form').submit();
            }
        }
    });
    function hasEmptyFields(form_groups){
        var empty = false;
        form_groups.each(function(){
            var input = $(this).find('input');
            var feedback = $(this).find('span');
            if(feedback.length && !input.val()){
                $(this).addClass('has-feedback has-warning');
                feedback.addClass('glyphicon-warning-sign');
                feedback.removeClass('hide');
                empty = true;
            }
        });
        return empty;
    };

    $('.form-group #handle').on({
    	keyup:function(){
            var current_handle = {'handle':$(this).val()};
    		var url_to_send = '/signup/check/handle';
            var success = function(data){
                if(data['valid'] && !data['registered']){
                    $('#handle-group').removeClass('has-warning');
                    $('#handle-feedback').removeClass('glyphicon-warning-sign');
                    $('#handle-group').addClass('has-feedback has-success');
                    $('#handle-feedback').addClass('glyphicon-ok');
                    $('#handle-feedback').removeClass('hide');
                }
                else{
                    $('#handle-group').removeClass('has-success');
                    $('#handle-feedback').removeClass('glyphicon-ok');
                    $('#handle-group').addClass('has-feedback has-warning');
                    $('#handle-feedback').addClass('glyphicon-warning-sign');
                    $('#handle-feedback').removeClass('hide');
                }
            };
            sendAjaxPost(current_handle,url_to_send,success);
    	},
        blur:function(){
            if(!$(this).val()){
                $('#handle-group').removeClass('has-success');
                $('#handle-feedback').removeClass('glyphicon-ok');
                $('#handle-group').addClass('has-feedback has-warning');
                $('#handle-feedback').addClass('glyphicon-warning-sign');
                $('#handle-feedback').removeClass('hide');
            }
        }
    });
    $('.form-group #email').on({
        blur:function(){
            var current_email = {'email':$(this).val()};
            var url_to_send = '/signup/check/email';
            var success = function(data){
              if(data['valid'] && !data['registered']){
                    $('#email-group').removeClass('has-warning');
                    $('#email-feedback').removeClass('glyphicon-warning-sign');
                    $('#email-group').addClass('has-feedback has-success');
                    $('#email-feedback').addClass('glyphicon-ok');
                    $('#email-feedback').removeClass('hide');
                }
                else{
                    $('#email-group').removeClass('has-success');
                    $('#email-feedback').removeClass('glyphicon-ok');
                    $('#email-group').addClass('has-feedback has-warning');
                    $('#email-feedback').addClass('glyphicon-warning-sign');
                    $('#email-feedback').removeClass('hide');
                }  
            };
            sendAjaxPost(current_email,url_to_send,success);
        }
    });
    $('.form-group #password').on({
           blur:function(){
                if(!$(this).val()){
                    $('#password-group').removeClass('has-success');
                    $('#password-feedback').removeClass('glyphicon-ok');
                    $('#password-group').addClass('has-feedback has-warning');
                    $('#password-feedback').addClass('glyphicon-warning-sign');
                    $('#password-feedback').removeClass('hide');
                }
            }
    });
    function sendAjaxPost(data_to_send,send_to_url,success_func){
    	$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		        }
		    }
		});
    	$.ajax({
    		url:send_to_url,
    		method:'POST',
    		data:data_to_send,
    		success:success_func
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