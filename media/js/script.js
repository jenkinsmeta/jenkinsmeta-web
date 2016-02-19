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


JenkinsMetaWebApp.controller('mainController', function($scope, $http) {

  var request = $http({
      method: 'POST',
      url: '/',
      data: {
          content: 'jobs'
      }
  });

  $scope.jobs = [];
  request.success(
      function( content ) {
          $scope.jobs = content;
      }
  );

})
.directive('singleBuild', function() {
  return {
    templateUrl: '/static/templates/single_build.html'
  };
});
