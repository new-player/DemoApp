(function(){
	'use strict';
	
	angular
		.module('demoapp', [		                    
		         'demoapp.routes',
		         'demoapp.authentication',
		         'demoapp.config',
		         'demoapp.layout']);
	
	angular
		.module('demoapp.routes', ['ngRoute']);
	
	angular
		.module('demoapp.config', []);
	
	angular
	  .module('demoapp')
	  .run(run);

	run.$inject = ['$http'];

	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	}
	
})();