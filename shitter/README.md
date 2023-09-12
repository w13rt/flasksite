# Shitter
This is 'social' media website
The use for this has yet to be found.

[the origonal tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

The main goal is to have it working and looking sorta nice without some `js` bullshit. So far so good

## how to start server
normal
`flask run`

debug
`flask run --debug`

## How to start shell
`flask shell`

This is used mainly to interact with the database, to, for example manually add new users

### "Data base interactions"
Because its kind of an inetersting selution, we manually have to add collums and rows sometimes
#### Migrations
`flask db migrate -m "followers"`
#### Update
`flask db update`
