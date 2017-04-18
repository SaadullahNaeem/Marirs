angular.module('ProjectApp')
    .controller('loginController', ['$scope', 'socialService', 'authService', '$auth', 'authFact', '$state',
        function ($scope, socialService, authService, $auth, authFact, $state) {

            if (authFact.isAuthenticated()) {}

            $scope.social_authentication = function (provider) {
                socialService.social_authentication_login(provider, $auth)
            }
            $scope.loginForm = function () {
                authService.login($scope.login_username, $scope.login_password).success(function (data) {
                    if (data.errors) {
                        var errors = data.errors;
                        $('.alert').remove();
                        for (i in errors) {
                            $('<div class="alert alert-danger alert-dismissable fade in"> <a class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>'+errors[i][0] + '</strong></div>').insertBefore($('#my_login_form'));
                            break;
                        }

                    } else {
                        authFact.buildCookies(data);
                        $state.go('home', {}, { reload: true });
                    }

                });
            }


        }]);
