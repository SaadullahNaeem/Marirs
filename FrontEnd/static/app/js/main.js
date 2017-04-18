var ProjectModule = angular.module( 'ProjectApp', ['ui.router', 'ngResource', 'satellizer','ngCookies']);

ProjectModule.config(['$stateProvider', '$urlRouterProvider', '$locationProvider', '$resourceProvider'
    , function ($stateProvider, $urlRouterProvider, $locationProvider, $resourceProvider) {

        // For any unmatched url, send to /logOutPage
        $urlRouterProvider
            .otherwise("/");

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/static/app/views/dashboard.html',
                controller: 'dashboardController'
            })
            .state('login', {
                url: '/login',
                templateUrl: 'static/app/views/login.html',
                controller: 'loginController'
            })
            .state('logout', {
                url: '/logout',
                controller: 'logoutController'

            })
            .state('signup', {
                url: '/signup',
                templateUrl: 'static/app/views/signup.html',
                controller: 'signupController'
            });

        $resourceProvider.defaults.stripTrailingSlashes = false;
        //$locationProvider.html5Mode(true);
    }])

    .run(['$rootScope', '$state', 'authFact', '$location', '$cookies', function ($rootScope, $state, authFact, $location, $cookies) {

        $rootScope.$on('$stateChangeSuccess', function () {
            document.body.scrollTop = document.documentElement.scrollTop = 0;
        });

        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {
            if (localStorage.getItem('JWT')) {
                $rootScope.userObj = $cookies.get('userObj');
            }
        });

        $rootScope.location = $location;

    }])

    .run(function run($http, $cookies) {
        // For CSRF
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
    })

    .config(['$httpProvider', function ($httpProvider) {
        $httpProvider.interceptors.push(['$rootScope', '$location', '$q', function ($rootScope, $location, $q) {
            return {
                'request': function (config) {
                    var auth = localStorage.getItem('JWT');
                    $rootScope.IsLoggedIn = false;

                    if (auth) {
                        config.headers.Authorization = 'JWT ' + auth;
                        $rootScope.IsLoggedIn = true;
                    }

                    return config
                },
                'responseError': function (response) {
                    if (response.status === 401 || response.status === 403) {
                        localStorage.removeItem('JWT');
                        $location.url('/');
                    }

                    return $q.reject(response);
                }
            }
        }])
    }]);

