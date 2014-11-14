$(function(){

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
});