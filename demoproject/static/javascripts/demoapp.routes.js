(function (){
	
	angular
		.module('demoapp.routes')
		.config(config)
		
	config.$inject = ['$routeProvider'];
	console.error('gdfhfd');
	
	function config($routeProvider) {
		$routeProvider.when('/register', {
			controller: 'RegisterController',
			controllerAs: 'vm',
			templateUrl: '/static/templates/authentication/register.html'
		}).when('/login', {
			  controller: 'LoginController',
			  controllerAs: 'vm',
			  templateUrl: '/static/templates/authentication/login.html'
		}).otherwise('/');
	}
})();