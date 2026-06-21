# SSL proxying for user content

> **Warning:** Untested on FreateOJ

User-generated content (e.g., comments) poses a threat to site security, and can cause mixed-content warnings. If your site is served over HTTPS, this may be suboptimal - routing user content through a secure server can help.

The FreateOJ site provides support for this through the Github Camo project, which requires CoffeeScript to be installed (`apt install coffeescript`).

> **Warning:** Setting up Camo on the same server as your site can leave you open to attacks, even if you are set up behind Cloudflare: a
> malicious user can link an image to their domain, have Camo access it, and then view their server logs to see the requesting
> IP (allowing them to attack you behind e.g. Cloudflare).
>
> If this is important in your scenario, consider running Camo on a separate server.

## Installing Camo to `/code`

```shell-session
$ cd /code
$ git clone Camo repository camo
```

Now, Camo may be started by running `/code/camo/server.coffee`.

```shell-session
$ PORT="<port>" CAMO_KEY="<key>" coffee /code/camo/server.coffee
```

- Camo will listen on `<port>`.
- `<key>` is the HMAC secret key used for digests. Set it to anything you want. This is used for cache-busting purposes, so it does not need to be secure.

## Configuring FreateOJ to use Camo

To enable the use of Camo in the FreateOJ site, you need to specify a couple of variables in your `local_settings.py`.

```python
# The URL on which Camo is listening
FREATEOJ_CAMO_URL = "https://example.com[:port]"
# The key you specified for running Camo
FREATEOJ_CAMO_KEY = "<key>"
# Domains to exclude from Camo proxying. Typically, these would be your own domains which you use
# for content delivery, and you know to already be secure.
FREATEOJ_CAMO_EXCLUDE = ("https://oj.freate.io.vn",)
# Whether Camo should use HTTPS for protocol neutral URIs (you probably want this)
FREATEOJ_CAMO_HTTPS = True
```

Restart FreateOJ for the changes to take effect. After restarting, you may have to purge Django's cache before seeing any changes.
