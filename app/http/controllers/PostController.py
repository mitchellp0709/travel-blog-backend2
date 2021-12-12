""" A PostController Module """

from masonite.controllers import Controller
from app.Post import Post
from masonite.request import Request

class PostController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request:Request):
      self.request=request

    def show(self):
        """Show a single resource listing
        ex. Model.find('id')
            Get().route("/show", PostController)
        """
        id= self.request.param("id")
        return Post.find(id)

    def index(self):
        """Show several resource listings
        ex. Model.all()
            Get().route("/index", PostController)
        """
        return Post.all()
        

    def create(self):
        """Show form to create new resource listings
         ex. Get().route("/create", PostController)
        """

        name = self.request.input("name")
        description=self.request.input("description")
        image=self.request.input("image")
        post = Post.create({"name":name,"description":description,"image":image,})
        
        return post

    def update(self):
        """Edit an existing resource listing
        ex. Post target to update new Model
            Post().route("/update", PostController)
        """

        id=self.request.param("id")
        name = self.request.input("name")
        description=self.request.input("description")
        image=self.request.input("image")
        post = Post.where("id",id).update({"name":name,"description":description,"image":image})
        return post

    def destroy(self):
        """Delete an existing resource listing
        ex. Delete().route("/destroy", PostController)
        """

        id = self.request.param("id")
        post= Post.where("id",id).get()
        Post.where("id",id).delete()
        return post