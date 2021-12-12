"""Web Routes."""

from masonite.routes import Get, Post, Put, RouteGroup, Delete

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/", "PostController@index").name("index"),
        Get("/@id", "PostController@show").name("show"),
        Post("/", "PostController@create").name("create"),
        Put("/@id", "PostController@update").name("update"),
        Delete("/@id", "PostController@destroy").name("destroy"),
    ], prefix="/posts", name="posts")
]
