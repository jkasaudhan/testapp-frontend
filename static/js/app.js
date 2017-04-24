$(document).ready(function() {
    var BASE_URL = 'http://127.0.0.1:5000/api/v1';
    
    $('#system-search').keyup(function(event) {
        if(!(/[a-zA-Z0-9]/.test(event.key))) {
            return;
        }else {
            searchAndRender(event.target.value.trim());
        }
    });
    
    var searchAndRender = function(keyword) {
        //Get data from backend based on the search key word
        $.get(BASE_URL+'/search/?query='+ keyword, function(data) {
            if(data.results.length !== 0) {
                $('.user-table tbody').empty();
                data.results.forEach(user => {
                    var row =   $('<tr><td>'+ user.id+'</td>' + 
                                '<td>'+ user.first_name +'</td>' +
                                '<td>' + user.last_name + '</td>' +
                                '<td>' + user.gender + '</td>' +
                                '<td>' + user.email + '</td>' +
                                '<td>' + user.job_title + '</td></tr>');
                   
                    $('.user-table tbody').append(row);
                });
            };
           
        });
    }

});