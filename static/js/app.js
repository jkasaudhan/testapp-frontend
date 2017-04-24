$(document).ready(function() {
    var BASE_URL = 'http://127.0.0.1:5000';
    
    //Initially display default user list using templating engine syntax {...} which is used in the home.html view so, we don't have to do anything here.
    
    //If user starts typing on search text box display filtered information
    $('#system-search').keyup(function(event) {
        var keyword = $('#system-search').val();
        if(!keyword) {
            //If keyword is cleared from the search box, than reset with the original default user's list
            reset();
        } else if(!validateSearchKey(keyword)) {
            return;
        }
        searchAndRender();
    });
    
    //Start searching when search button is clicked
    $('.search-btn').click(function() {
        var keyword = $('#system-search').val();
        //If keyword is empty reset the view with default data
        if(!keyword) {
            reset();
        }
        
        if(!validateSearchKey(keyword)) {
            return;
        }
        searchAndRender();
    });
    
    //Returns true if the string is alphanumeric string
    var validateSearchKey = function(key) {
        if((/^[a-z0-9]+$/i.test(key))) {
            return true;
        }else {
            return false;
        }
    }
    
    var searchAndRender = function() {
        var keyword = $('#system-search').val();
        var sortByParam =  $('#sel1').val();
        var orderByParam = $('#sel2').val();
        
        if(!keyword) {
            //If search keyword is not present, use default sort endpoint
            var endpoint = BASE_URL+'/api/v1/sort/?sort_by='+ sortByParam +'&order='+ orderByParam;
            $.get(endpoint, function(response) {
                renderOnView(response.results);
            });
        } else {
            //Get data from backend based on the search key word
            var endpoint = BASE_URL+'/api/v1/search/?query='+ keyword + '&sort_by=' + sortByParam +'&order='+ orderByParam;
            $.get(endpoint, function(response) {
                renderOnView(response.results);
            });
        }        
    }

    //Accepts user data and populates on the table view
    var renderOnView = function(data) {
        if(data.length !== 0) {
            $('.user-table tbody').empty();
            data.forEach(user => {
                var row =   $('<tr class="user-row" data-id="'+ user.id +'"><td>'+ user.id+'</td>' + 
                            '<td>'+ user.first_name +'</td>' +
                            '<td>' + user.last_name + '</td>' +
                            '<td>' + user.gender + '</td>' +
                            '<td>' + user.email + '</td>' +
                            '<td>' + user.job_title + '</td></tr>');

                $('.user-table tbody').append(row);
            });
        };
    }
    
    //Sort using the parameters used on the select options
    $('#sel1').change(function(event) {
        searchAndRender();
    });
    
    $('#sel2').change(function(event) {
        searchAndRender();
    });
    
    //When search field is cleared reset table data to default user's list 
    var reset = function() {
        $('#sel1').val('id');
        $('#sel2').val('asc');
        searchAndRender();
    }
    
    //When user clicks on any row redirect them to user detail page view: (using event delegation)
    $('.user-table tbody').click(function(event) {
        var userID = $(event.target).parent().first().data('id');
        if(userID) {
            window.location = BASE_URL+'/view/' + userID;
        }
    });
});