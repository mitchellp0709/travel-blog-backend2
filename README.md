# Travel Blog Front End 

### By J. Mitchell Paoletti


## Project Summary

A place for users to upload a photo, title, and description of their trip. Wherever they travel, they can tell a story of what they did and where they went. 

## Post Schema

- Title (string) - title of the post
- Description (string) - description of the post
- Image (string) - link to the image associated with the post 

## Route Table

| url | method | action |
|-----|--------|--------|
| /posts | get | show all posts (index)|
| /posts/id | get | show specific post posts (show)|
| /posts | post | create a new post (create)|
| /posts/id | put | edit specific post by id (update)|
| /posts/id | delete | delete a specific post by id (delete)|

## Challenges

My biggest challenge was to get the user authorization implemented. I continued getting errors so in the interest of getting this project completed on time, it had to be dropped.

## List of Technologies

- Python
- Postgres
- Masonite