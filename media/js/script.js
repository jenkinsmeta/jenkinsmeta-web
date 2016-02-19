var JenkinsMetaWebApp = angular.module('JenkinsMetaWebApp', ['ngRoute']);

JenkinsMetaWebApp.config(function ($interpolateProvider) {
  $interpolateProvider
    .startSymbol('{[{')
    .endSymbol('}]}')
});

JenkinsMetaWebApp.config(function ($routeProvider) {
  $routeProvider
    .when('/builds', {
      templateUrl : '/static/templates/builds.html', 
      controller : 'mainController'
    })
});

JenkinsMetaWebApp.controller('mainController', function($scope, $http) {
  $scope.get_content = function( endpoint ) {
    $http({
      method: 'POST',
      url: '/',
      data: {
        endpoint: endpoint
      }
  })
    .success(
      function( content ) {
          $scope.jobs = content;
      })
    .error(
      function( content ) {
          $scope.jobs = {}
      });
  };

  $scope.get_content('jobs');

})
.directive('singleBuild', function() { return { templateUrl: '/static/templates/single_build.html' };
});
