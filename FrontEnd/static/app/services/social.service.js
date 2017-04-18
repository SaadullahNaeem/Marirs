angular.module('ProjectApp')
 .service('socialService', ['authFact', '$state', function(authFact, $state){
      var social = {};
      social.social_authentication = function(provider, $auth){
          $auth.authenticate(provider).then(function(response){
            source = response.data
            var payload = {
                    first_name: source.username,
                    email:  source.email,
                    password1:'Panasonic',
                    password2:'Panasonic'
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

        }).catch(function(data) {
            var err_msg = data.data.error;
            console.log(data)
            console.log(err_msg);
            alert(err_msg);
        });
      }
       social.social_authentication_login = function(provider, $auth){
          $auth.authenticate(provider).then(function(response){
            source = response.data
            authService.login(source.email, 'Panasonic').success(function (data) {
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
        }).catch(function(data) {
            var err_msg = data.data.error;
            console.log(data)
            console.log(err_msg);
            alert(err_msg);
        });
      }
      return social;
 }])