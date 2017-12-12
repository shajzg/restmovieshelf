(function(){

    var app = angular.module("movieshelf",[]);

    app.config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
     });

}());
