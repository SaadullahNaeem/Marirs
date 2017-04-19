angular.module('ProjectApp')
    .controller('dashboardController', ['$scope', 'socialService', 'authService', '$auth', 'authFact', '$state','$cookies', '$http','$timeout',
        function ($scope, socialService, authService, $auth, authFact, $state, $cookies, $http,$timeout) {

            // if (authFact.isAuthenticated()) { }
            $scope.myFunc=function(){
            	alert('saad');
            }
        }]);
