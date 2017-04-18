angular.module('ProjectApp')
 .service('authService', ['$http', function($http){
     var Auth = {};

     Auth.resetPassword = function(email){
         var payload = $.param({
             'email': email
         });

         return $http({
             method: 'POST',
             url: '/accounts/forget/password/',
             data: payload,
             headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}  
         })
     }

     Auth.login = function(username, password){
         $('form[name="login_form"]').find('.alert').remove();
         var payload = {
             username: username,
             password: password
         }

         return $http.post('/accounts/signin/', payload);
     }

     Auth.register = function(payload){
         $('form[name="register_form"]').find('.alert').remove();
          return $http.post('/accounts/register/', payload);
     }

     return Auth;
 }]);