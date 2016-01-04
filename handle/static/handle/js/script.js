$(document).ready(function(){
    $(".handle-tooltip").tooltip({title: "Profile and more",placement:'bottom'});

    $('#privacy-lock').click(function(e){
        e.preventDefault();
        var lock = $(this).children('span');
        if(lock.hasClass('glyphicon-eye-close')){
            lock.removeClass('glyphicon-eye-close');
            lock.addClass('glyphicon-eye-open');
            $(this).attr({title:'Email Public'});
        }
        else{
            lock.removeClass('glyphicon-eye-open');
            lock.addClass('glyphicon-eye-close');
            $(this).attr({title:'Email Private'});
        }
    });

    $('#add-challenge-btn').click(function(e){
        e.preventDefault();
    });

    $('#testcase-submit').click(function(e){
        e.preventDefault();
        data_to_send = {
            'input':$('#sample-in').val(),
            'output':$('#sample-out').val()
        };
        url_to_send = '/recent/new/testcase';
        $("#testcase-modal").modal('hide');
    });

    $('#signup-btn').click(function(e){
    	e.preventDefault();
        var form_groups = $('#signup-form').children('div');
        var validated = {}
        if(!hasEmptyFields(form_groups)){
            if(!validated['password']){
                current_password = $('#password').val();
                if(isValidPass(current_password)){
                    validField('password-group','password-feedback');
                    validated['password'];
                }
                else{
                    invalidField('password-group','password-feedback');
                }
            }

            form_groups.each(function(){
                var feedback = $(this).find('span');
                if(feedback.hasClass('glyphicon-ok')){
                    var key = $(this).find('input')[0]['id'];
                    validated[key]=true;
                }
            });
            
            if(validated['handle'] && validated['email'] && validated['password']){
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

    var recent_handles = {}
    $('.form-group #handle').on({
    	keyup:function(){
            var handle = $(this).val();
            if(handle.trim().length >= 3 && !recent_handles[handle]){
                var current_handle = {'handle':handle};
        		var url_to_send = '/signup/check/handle';
                var success = function(data){
                    if(data['handle']){
                        validField('handle-group','handle-feedback');
                        recent_handles[handle] = 'available';
                    }
                    else{
                        invalidField('handle-group','handle-feedback');
                        recent_handles[handle] = 'unavailable';
                    }
                };
                sendAjaxPost(current_handle,url_to_send,success);
        	}
            else if(handle){
                if(recent_handles[handle] == 'available'){
                    validField('handle-group','handle-feedback');
                }
                else{
                    invalidField('handle-group','handle-feedback');
                }
            }
            else if(Object.keys(recent_handles).length != 0){
                invalidField('handle-group','handle-feedback');
            }
        }
    });
    
    function isValidEmail(email){
        regex = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
        return regex.test(email);
    }
    
    function isValidPass(password){
        regex = /^[a-zA-Z0-9]{6,}$/;
        return regex.test(password);
    }

    function validField(group_id,feedback_id){
        $('#'+group_id).removeClass('has-warning');
        $('#'+feedback_id).removeClass('glyphicon-warning-sign');
        $('#'+group_id).addClass('has-feedback has-success');
        $('#'+feedback_id).addClass('glyphicon-ok');
        $('#'+feedback_id).removeClass('hide');
    }

    function invalidField(group_id,feedback_id){
        $('#'+group_id).removeClass('has-success');
        $('#'+feedback_id).removeClass('glyphicon-ok');
        $('#'+group_id).addClass('has-feedback has-warning');
        $('#'+feedback_id).addClass('glyphicon-warning-sign');
        $('#'+feedback_id).removeClass('hide');
    }

    $('.form-group #email').on({
        blur:function(){
            var email = $(this).val();
            if(email.trim()){
                var current_email = {'email':email};
                var url_to_send = '/signup/check/email';
                var email_flag = isValidEmail(email);
                var success = function(data){
                    if(email_flag && data['email']){
                        validField('email-group','email-feedback');
                    }
                    else{
                       invalidField('email-group','email-feedback');
                    }  
                };
                sendAjaxPost(current_email,url_to_send,success);
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
    
    function sendAjaxPost(data_to_send,send_to_url,success_func){
        $.ajax({
            url:send_to_url,
            method:'GET',
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