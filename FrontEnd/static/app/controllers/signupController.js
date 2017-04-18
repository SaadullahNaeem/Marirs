angular.module('ProjectApp')
    .controller('signupController', ['$scope', 'socialService', 'authService', '$auth', 'authFact', '$state',
        function ($scope, socialService, authService, $auth, authFact, $state) {

            if (authFact.isAuthenticated()) {}

            $scope.social_authentication = function (provider) {
                socialService.social_authentication(provider, $auth)
            }

            $scope.registerForm = function () {
                var payload = {
                    email: $scope.register_form.email,
                    password1: $scope.register_form.password1
                }

                authService.register(payload).success(function (data) {
                    if (data.errors) {
                        var errors = data.errors;
                        $('.alert').remove();
                        for (i in errors) {
                               $('<div class="alert alert-danger alert-dismissable fade in"> <a class="close" data-dismiss="alert" aria-label="close">&times;</a><strong>'+errors[i][0] + '</strong></div>').insertBefore($('#my_signup_form'));
                                break;
                           }

                        $state.go('signup', { reload: true });
                    } else {
                        authFact.buildCookies(data);
                        $state.go('home', { reload: true });
                    }
                })
            }

        }]);
