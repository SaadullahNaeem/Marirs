angular.module('ProjectApp')
    .factory('authFact', ['$cookies', '$state', '$http', '$location', function ($cookies, $state, $http, $location) {

        var authFact = {};
        var authKey = 'JWT';

        authFact.setAccessToken = function (accessToken) {
            //$cookies.put('accessToken', accessToken);
            localStorage.setItem(authKey, accessToken);
        };

        authFact.getAccessToken = function () {
            authFact.authToken = localStorage.getItem(authKey);
            return authFact.authToken;
        };

        authFact.setUserObj = function (userObj) {
            $cookies.put('user_name', userObj.user_name);
            $cookies.put('email', userObj.email);
            $cookies.put('user_id', userObj.user_id);
        }

        authFact.getUserObj = function () {
            var userObj = $cookies.get('user_name');
            if (userObj)
                return userObj;
        };

        authFact.navigateToHome = function () {
            $state.go('pickHotNotPage');
        };

        authFact.buildCookies = function (data) {
            userObj = {};
            userObj.user_name = data.user_name;
            userObj.email = data.email;
            userObj.user_id = data.user_id;
            authFact.setUserObj(userObj);
            // Set token to localStorage
            authFact.setAccessToken(data.access_token);
        }

        authFact.destroyCookies = function () {
            localStorage.removeItem(authKey);

            $cookies.remove('email');
            $cookies.remove('user_name');
        };

        authFact.isAuthenticated = function () {

            var access_token = localStorage.getItem(authKey);
            if(access_token){
                $('#in').hide();
                $('#up').hide();
                $('#out').show();

            }
            if (['/signup'].indexOf($location.path()) == -1) {
                if (!access_token) {

                    $('#in').show();
                    $('#up').show();
                    $('#out').hide();

                    $state.go('login');
                }
            }
        }

        authFact.logout = function () {
            $http({
                method: 'GET',
                url: '/logout/',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
            })
                .success(function (data) {
                    authFact.destroyCookies();
                    $state.go('login', { reload: true });
                });
        };

        authFact.postToServer = function (dataToServer) {
            var userInfo = $.param(dataToServer);

            remove_errors = $('p.error').remove();

            current_action_url = dataToServer.url;

            if (current_action_url == 'login') {
                $http({
                    method: 'POST',
                    url: '/accounts/signin/',
                    data: userInfo,
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
                })
                    .success(function (data) {
                        alert();
                        console.log(data);
                        if (data.errors) {
                            var errors = data.errors;
                            for (i in errors) {
                                if (i == '__all__') {
                                    $('<p class="error">' + errors[i][0] + '</p>').insertBefore($('#id_email'));
                                }
                            }
                        } else {
                            // if successful, bind success message to message
                            authFact.buildCookies(data);
                            $state.go('pickHotNotPage', { reload: true });
                        }

                    });
            }

            if (current_action_url == 'register') {
                $http({
                    method: 'POST',
                    url: '/accounts/register/',
                    data: userInfo,
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
                })
                    .success(function (data) {
                        if (data.errors) {
                            var errors = data.errors;
                            for (i in errors) {
                                $('<p class="error">' + errors[i][0] + '</p>').insertAfter($('#id_' + i));
                            }
                        } else {
                            // if successful, bind success message to message
                            authFact.buildCookies(data);
                            $state.go('pickHotNotPage', { reload: true });
                        }
                    });
            }

            if (current_action_url == 'social-login') {
                $http({
                    method: 'POST',
                    url: '/social/login/',
                    data: userInfo,
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
                })
                    .success(function (data) {
                        if (data.errors) {
                            var errors = data.errors;
                            for (i in errors) {
                                $('<p class="error">' + errors[i][0] + '</p>').insertAfter($('#id_' + i));
                            }
                        } else {
                            // if successful, bind success message to message
                            userObj = {};
                            userObj.user_name = data.user_name;
                            userObj.email = data.email;
                            authFact.setAccessToken(data.access_token);
                            authFact.setUserObj(userObj);
                            $state.go('pickHotNotPage', { reload: true });
                        }
                    });
            }

            if (current_action_url == 'forget-password') {
                $scope.IfSuccess = false;

                $http({
                    method: 'POST',
                    url: '/accounts/forget/password/',
                    data: userInfo,
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
                })
                    .success(function (data) {
                        if (data.errors) {
                            var errors = data.errors;
                            for (i in errors) {
                                $('<p class="error">' + errors[i][0] + '</p>').insertAfter($('#id_' + i));
                            }
                        } else {
                            // if successful, bind success message to message
                            $scope.IfSuccess = true;

                        }
                    });
            }

        };

        return authFact;

    }]);