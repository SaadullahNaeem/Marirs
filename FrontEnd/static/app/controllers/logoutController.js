angular.module('ProjectApp')
    .controller('logoutController', ['$scope', 'socialService', 'authService', '$auth', 'authFact', '$state',
        function ($scope, socialService, authService, $auth, authFact, $state) {

                authFact.logout();

        }]);
