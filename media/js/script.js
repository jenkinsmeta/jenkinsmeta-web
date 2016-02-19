var JenkinsMetaWebApp = angular.module('JenkinsMetaWebApp', ['ngRoute']);

JenkinsMetaWebApp.config(function ($interpolateProvider) {
  $interpolateProvider
    .startSymbol('{[{')
    .endSymbol('}]}')
});

JenkinsMetaWebApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl : '/static/templates/builds.html', 
      controller : 'mainController'
    });
});

JenkinsMetaWebApp.controller('mainController', function($scope) {
  $scope.message = 'Single menu item';
});
