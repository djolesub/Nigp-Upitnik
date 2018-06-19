$(document).ready(function(){

    /*Java Script for adding, updating and deleting forms from formset*/

    function updateElementIndex(el, prefix, ndx) {
        var id_regex = new RegExp('(' + prefix + '-\d+)');
        var replacement = prefix + '-' + ndx;
        
        if ($(el).attr("for"))
            $(el).attr("for", $(el).attr("for").replace($(el).attr("for"), replacement));
            
        if (el.id) {
        prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
            d = 'id_' + prefix_for_new_rows + el.id.substring(22, el.id.length)
            el.id = d;
            var div = $(el).next();
            var div1 = div.children('div');
            var input_final = div1.children('input');
            input_final.attr('id', el.id+"_ostalo")
            div.css('display','none');
           
            
        }

        if (el.name) {
            
            prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
            d = prefix_for_new_rows + el.name.substring(19, el.name.length)
            el.name = d;
            var div = $(el).next();
            var div1 = div.children('div');
            var input_final = div1.children('input');
            input_final.attr('name', el.name+"_ostalo")
            
            
        }
        
        
    };

    function addForm(btn, prefix, cname) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        var row = $('.' + cname + ':first').clone(false).get(0);
        
        $(row).removeAttr('id').insertAfter($('.' + cname + ':last')).children('.hidden').removeClass('hidden');
        
        $(row).children().not(':last').children().each(function(index,element) {
            
            updateElementIndex(this, prefix, formCount);
            
           
        });
        
        var select_formsets = $("select[name*='formset'][name^='pitanje']");
        
        $(select_formsets).each(function(i,e){
            
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
        });

        var a = $(row).children().children();
        console.log(a);
        $(row).children().children().each(function(){
            if($(this).hasClass('jedinstveni')){
               // alert("has class Jedinstveni");
                prefix_for_new_rows = prefix + '-' + $('#id_' + prefix + '-TOTAL_FORMS').val()
                id = 'id_' + prefix_for_new_rows + '-Jedinstveni';
                name = prefix_for_new_rows + '-Jedinstveni';
                this.id = id 
                this.name = name

            }
        });
        
        var nt = prefix.substring(0,10); 
        $(row).find('.delete-row_'+nt).click(function() {
           
            deleteForm(this, prefix, cname);
        });
        $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
        return false;
    };

    function deleteForm(btn, prefix, cname) {
        $(btn).parents('.' + cname).remove();
        var forms = $('.' + cname);
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i = 0, formCount = forms.length; i < formCount; i++) {
            $(forms.get(i)).children().not(':last').children().each(function() {
                updateElementIndex(this, prefix, i);
            });
        }
        return false;
    }

    /***********************************************************************************************************/

    //Pitanje2_8Formset form5 
    $('.add-row_pitanje2_8').click(function() {
        return addForm(this, 'pitanje2_8formset', 'dynamic-form-pitanje2_8');
    });
    $('.delete-row_pitanje2_8').click(function() {
        return deleteForm(this, 'pitanje2_8formset', 'dynamic-form-pitanje2_8');
    })

    //Pitanje2_6Formset form4 
    $('.add-row_pitanje2_6').click(function() {
        return addForm(this, 'pitanje2_6formset', 'dynamic-form-pitanje2_6');
    });
    $('.delete-row_pitanje2_6').click(function() {
        alert("Djordje Delete");
        return deleteForm(this, 'pitanje2_6formset', 'dynamic-form-pitanje2_6');
    })

    //Pitanje2_5Formset form3 
    $('.add-row_pitanje2_5').click(function() {
        return addForm(this, 'pitanje2_5formset', 'dynamic-form-pitanje2_5');
    });
    $('.delete-row_pitanje2_5').click(function() {
        return deleteForm(this, 'pitanje2_5formset', 'dynamic-form-pitanje2_5');
    })

    //Pitanje3_3Formset form12 
    $('.add-row_pitanje3_3').click(function() {
        return addForm(this, 'pitanje3_3formset', 'dynamic-form-pitanje3_3');
    });
    $('.delete-row_pitanje3_3').click(function() {
        return deleteForm(this, 'pitanje3_3formset', 'dynamic-form-pitanje3_3');
    })

    //Pitanje3_3Formset form14
    $('.add-row_pitanje3_5').click(function() {
        return addForm(this, 'pitanje3_5formset', 'dynamic-form-pitanje3_5');
    });
    $('.delete-row_pitanje3_5').click(function() {
        return deleteForm(this, 'pitanje3_5formset', 'dynamic-form-pitanje3_5');
    })

    //Pitanje5_2Formset form19
    $('.add-row_pitanje5_2').click(function() {
        return addForm(this, 'pitanje5_2formset', 'dynamic-form-pitanje5_2');
    });
    $('.delete-row_pitanje5_2').click(function() {
        return deleteForm(this, 'pitanje5_2formset', 'dynamic-form-pitanje5_2');
    })

    $(".selectpicker").selectpicker({
        style : "btn-default"

    });

	$("#id_form2-Broj_zaposlenih").on('blur', function(){
       		var a = $(this).val();
       		if (a <= 0) {
            		alert('Унели сте негативну вредност, биће конвертована у позитивну.');
            		$(this).val(Math.abs($(this).val()));
      		 }
    	});



    $('#btnPosalji').on('click',function(e){
       
        e.preventDefault()
        var jedinstveni = $('#id_form1-Naziv_organizacije').val(); 
        $('.jedinstveni').val(jedinstveni); 
        //conosle.log($('#formUpitnik').serializeArray());
        $('#formUpitnik').submit();
       
    });

    /*popover za Aneks pitanja*/ 
    $('[data-toggle="popover"]').popover();
    
    

});
