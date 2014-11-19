$(function(){

    //login like employee and company
    if(!$("#id_is_company").is(':checked')){
        $("#div_id_company_name").toggle(false);
    }
    else{
        $("#div_id_first_name").toggle(false);
        $("#div_id_last_name").toggle(false);
    }

    $('#id_is_company').click(function(){
        $("#div_id_first_name").toggle(!$("#id_is_company").is(':checked'));
        $("#div_id_last_name").toggle(!$("#id_is_company").is(':checked'));
        $("#div_id_company_name").toggle($("#id_is_company").is(':checked')).removeClass('invisible');
    });


    //jop post applying messages
    bootstrap_alert = function() {}
    bootstrap_alert.warning = function(message, is_error) {
        if(is_error) {
            $('#alert_placeholder').html('<div class="alert alert-danger"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')
        }else{
            $('#alert_placeholder').html('<div class="alert alert-success"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')
        }
    }


    //jop post applying via ajax
    var frm = $('#apply_form');
    frm.submit(function (e) {
        e.preventDefault();
        $('ul.errorlist').html("");
        var data = new FormData($('#apply_form').get(0));
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: data,
            processData: false,
            contentType: false,
            success: function (data) {
                if(data.notification) {
                    $('#applyModal').modal('hide');
                    bootstrap_alert.warning(data.notification, false);
                }
                else if(data.warning) {
                    $('#applyModal').modal('hide');
                    bootstrap_alert.warning(data.warning, true);
                }else if(data.error){
                    var form_errors = data.error;
                    for(var fieldname in form_errors) {
                        var errors = form_errors[fieldname];
                        $('#apply_form ul.errorlist').append('<li>'+ errors +'</li>')
                        $('#apply_form input[name="'+fieldname+'"]').addClass('error');
                    }
                }
            },
            error: function(data) {
                console.log(data);
            }
        });
    return false;
    });

    //job post applying form validation
    $('#id_message').click(function(){
        $('ul.errorlist').html("");
        $(this).removeClass("error");
    });
});

