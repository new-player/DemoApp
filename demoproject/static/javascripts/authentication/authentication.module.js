(function (){
	'use strict';
	
	angular
		.module('demoapp.authentication', [
		        'demoapp.authentication.controllers',
		        'demoapp.authentication.services']);
	
	angular
		.module('demoapp.authentication.controllers', []);
	
	angular
		.module('demoapp.authentication.services', ['ngCookies']);
})();
