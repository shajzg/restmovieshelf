
 var app = angular.module("movieshelf");

 var MainController = function($scope,$http,$log){
    $scope.title = "John's Movieshelf";
    $scope.copyright = "(C) John Zhang 2017";
    $scope.searchtype = "entitle";
    $scope.moviecontent = "";
    $scope.movieSortOrder = "-fields.year"
    $scope.reverse = true;

    var onMovieList = function(response){
        $scope.movies = response.data;
    };

    $scope.search = function(moviecontent,searchtype){
        var req = {
            method: 'POST',
            url: '/pymovieshelf/searchmovie/',
            data: {
                moviecontent: moviecontent,
                searchtype: searchtype,
            },
        };
        $http(req)
        .then(onMovieList);
    };

    $scope.search($scope.moviecontent,$scope.searchtype);
 };

 app.controller("MainController",MainController);
