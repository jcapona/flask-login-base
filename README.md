# Flask Login Base

Small app that manages user auth using flask-login. Also uses flask blueprints patterns to manage routes, and jinja as a template engine.

It's based on [this article](https://scotch.io/tutorials/authentication-and-authorization-with-flask-login), with some mods according to my needs.

## How to use?

Install dependencies from *requirements.txt*

Set proper environment variables:

```sh
export FLASK_APP=api
export FLASK_DEBUG=1
export SQLALCHEMY_DATABASE_URI=postgresql://<USERNAME>:<PASSWORD>@localhost:5432/<DB_NAME>
export SECRET_KEY=<SECRET-KEY>
export DEBUG=True
```

And run with `flask run`

## References

- [Flask blueprints docs](http://flask.pocoo.org/docs/1.0/blueprints/)
- [Flask configuration docs](http://flask.pocoo.org/docs/1.0/config/)
- [Scotch.io article](https://scotch.io/tutorials/authentication-and-authorization-with-flask-login)
- [BULMA.io docs](https://bulma.io/documentation/layout/hero/)
- [WTForms docs](https://wtforms.readthedocs.io/en/latest/validators.html#built-in-validators)

