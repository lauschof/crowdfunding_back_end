# Crowdfunding Back End
Laura

## Planning:
### Concept/Name
NeighbourhoodFund, https://neighbourhoodfund-b64a3fc78896.herokuapp.com/

This project is a community-driven crowdfunding platform designed to support local, small-scale projects in Perth, WA. Users can create or contribute to a variety of neighbourhood initiatives, from organising social events to implementing environmental improvements like recycling programs. The platform allows users to filter projects by suburb, making it easy to find and support causes close to home. 

### Intended Audience/User Stories
{{ Who are your intended audience? How will they use the website? }}

### Front End Pages/Functionality
-Homepage
    -see lists of available CF-projects
-Login/Sign Up section
    -allow users to log into their account
    -sign up: create a new user account
-My profile section
    -see details of user account
    -change details of users account
-Projects section
    - see details of created projects or pledges made
    -see saved projects
    -delete a created project
    -cancel a pledge

### API Spec
 URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| --- | ----------- | ------- |------------ | --------------------- | ---------------------------- |
|   /users/  |   POST |   Create a new account    | { "username": "string", "email": "string", "password": "string" }  | 201 | Created N/A
 /login/ (not completed)  |    POST   |   User Login    |    { "username": "string", "password": "string" }  |  200 OK  |  N/A
| /users/{id}/  |  GET   |   Get user details  |  NONE   |   200 OK   | User-specific authorisation
| /projects/  |  GET  |   List all available projects  |   None  | 200 OK  |  N/A
| /projects/  | POST   |    Create a new project  |    { "title": "string", "description": "string", "image": "string", "target_amount": "decimal",        "is_open": "boolean" }      |     201 Created |   Authentication required
|/projects/{id}   |  GET   |   Get project details  |     None      |    200 OK   |     N/A
|/projects/{id}  |  PUT     |   Update a project  |    { "title": "string", "description": "string", "image": "string", "target_amount": "decimal", "is_open": "boolean" }  | 200 OK     |   Project owner authorisation
|/projects/{id}/  |     DELETE  |  Delete a project    |      None      |    204 No Content  |  Project owner authorisation
|/projects/{id}/pledges/   |    GET  | List all pledged for a project |  None 200 |  OK N/A
|/pledged/  | POST  | Create a pledge for a project   |   { "amount": "decimal", "project": "string", "supporter": "string", "is_anonymous": "boolean", "comment": "string" }    |   201 v Created Authentication required
| /pledges/{id}/  |  GET  | Get pledge details  |  None    |  200 OK  |  Pledge creator or project owner authorisation
| /pledges/{id}/saved_projects/   |  GET  |     Saved projects    | None    |     200 OK  User-specific authorisation | 
| /pledges/{id}/saved_projects/  | POST  |  Save a project for later reference   | { "project_id": "string" }   | 201 Created    |   authentication required
| /pledges/{id}/saved_projects/  | DELETE  | Remove a project from saved list  | None 204 No content  |  User-specific authorisation

### DB Schema
/Users/lauraschofield/SheCodes/django/crowdfunding_back_end/images
