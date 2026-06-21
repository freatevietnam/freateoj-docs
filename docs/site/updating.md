# Updating the site

The FreateOJ is under active development, so occasionally you may wish to update. This is a fairly simple process.

> **Warning:** The FreateOJ development team makes no commitment to backwards compatibility. It's possible that an update migration
> might add, change, or delete data from your install. Always back up before attempting an update.
>
> If in doubt, feel free to contact us on Discord.

First, switch to the site virtual environment, and pull the latest changes.

```
(freateojsite) $ git pull origin master
```

Dependencies may have changed since the last time you updated, so install any missing ones now.

```
(freateojsite) $ pip3 install -r requirements.txt
```

The database schema might also have changed, so update it.

```
(freateojsite) $ ./manage.py migrate
(freateojsite) $ ./manage.py check
```

Finally, update any static files that may have changed.

```
(freateojsite) $ ./make_style.sh
(freateojsite) $ ./manage.py collectstatic
(freateojsite) $ ./manage.py compilemessages
(freateojsite) $ ./manage.py compilejsi18n
```

That's it! You may wish to condense the above steps into a script you can run at a later time.
