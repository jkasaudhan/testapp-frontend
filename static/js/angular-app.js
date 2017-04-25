angular.module('test-app',[])
       .controller('UserController', UserController)
       .factory('UserService', UserService)
       .constant('BASE_URL', 'http://127.0.0.1:5000');

UserController.$inject = ['$scope', 'UserService'];
function UserController($scope, UserService) {
    console.log('User controller called');
    $scope.userData = [];
    var keyword = $('#system-search').val();
    var sortByParam =  $('#sel1').val();
    var orderByParam = $('#sel2').val();
    
    $scope.onSearchFieldChange = function() {
        console.log('typing...');
        UserService.getUsers(keyword, sortByParam, orderByParam, function(res) {
            console.log("users from service", res);
            if(res.status === 200) {
                $scope.userData = res.data.results;
            }
            
        }, function(err) {
            console.error(err);
        });        
    }
    

    
}

UserService.$inject = ['$http', 'BASE_URL'];
function UserService($http, BASE_URL) {
    var getUsers = function(keyword, sortByParam, orderByParam, success, error) {
       //Get data from backend based on the search key word
        var endpoint = BASE_URL+'/api/v1/search/?query='+ keyword + '&sort_by=' + sortByParam +'&order='+ orderByParam;
        var req = {
             method: 'GET',
             url: endpoint,
             data: {}
        }
        
        $http(req).then(function(response) {
           success(response);
        }, function(err) {
            error(err);
        });
    }
    
    return {
        getUsers: getUsers
    };
    
}