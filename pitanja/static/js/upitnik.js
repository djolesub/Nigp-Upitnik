$(document).ready(function(){
    
    var input_ends_with_ostalo = $("input[name*='formset'][type!='hidden'][name$='ostalo']");
    var select_formsets = $("select[name*='formset'][name^='pitanje']");
    
    $(select_formsets).each(function(i,e){
        //console.log(e);
        var last_option = $('#'+$(e).attr('id')+' option:last-child');

        $(e).on('change', function(event){
            
            var elems_selected = $('#'+$(e).attr('id')+' option:selected');
            $(elems_selected).each(function(index, elem){
                if($(this).val() =="Друго" || $(this).val() == "Остало"){
                    console.log($(this).val());
                    var show_hide_div = $(e).attr('id')+'_ostalo';
                    $('#'+show_hide_div).css('display','block')
                }
                else{
                    console.log("ne");
                    var show_hide_div = $(e).attr('id')+'_ostalo';
                    $('#'+show_hide_div).css('display','none')
                }
            });

        })
        console.log("=======================================");
    });

    
    


});
