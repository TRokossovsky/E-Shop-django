function Accs() {
    var reveal = $('.accs');
    var accs_status = window.getComputedStyle(reveal[0]);
    if(accs_status.display == 'none') {
        $('.accs').show();
    } else {
        $('.accs').hide();
    } 
}

function Aside() {
    var aside_var = $('#catalogue-menu');
    var aside_status = window.getComputedStyle(aside_var[0]);
    if(aside_status.display == 'none') {
        $('#catalogue-menu').show();
    } else {
        $('#catalogue-menu').hide();
    } 
}

