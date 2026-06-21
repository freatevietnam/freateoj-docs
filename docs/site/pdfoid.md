# PDF generation of problem statements

The FreateOJ supports rendering problem statements to PDF. This can be useful in the case of on-site contests, where
contestants receive paper versions of the problems.

PDF generation is backed by a related project, Pdfoid. Pdfoid interfaces with
Selenium to provide a REST endpoint for PDF rendering.

## Installing Pdfoid

First, clone the Pdfoid repository, and install it and its dependencies into a new virtualenv.

```shell-session
$ git clone Pdfoid repository
$ cd pdfoid
$ python3 -m venv env
$ . env/bin/activate
$ pip install -e .
```

Install `exiftool`, which is used to set PDF titles.

```shell-session
$ apt install exiftool
```

Install ChromeDriver, a special version of the Chromium engine needed by
Selenium to create PDFs.

```shell-session
$ apt install chromium-driver
```

## Running Pdfoid

To start the Pdfoid server, run:

```shell-session
$ export CHROME_PATH=<path to chrome>
$ export CHROMEDRIVER_PATH=<path to chromedriver>
$ export EXIFTOOL_PATH=<path to exiftool>
$ env/bin/pdfoid --port=<port>
```

The environment variables are not necessary if all three executables are present in `$PATH`, as they should be if you
followed the installation instructions above.

To test, start Pdfoid with `--port=8887`. Then, we can request a render of a simple HTML document.

```html
<div>Hello, World!</div>
```

The response should contain JSON, with a Base64-encoded PDF inside.

```shell-session
$ curl -d "title=Hello&html=Hello, World" -X POST -H "Content-Type: application/x-www-form-urlencoded" http://localhost:8887
{
    "success": true,
    "pdf": "JVBERi0xLjQKJdPr6eEKMSAwIG9iago8PC9DcmVhdG9yIChDaHJvbWl1bSkK..."
}
```

> **Note:** The FreateOJ uses a Segoe UI font when viewed on Windows browsers. If running Pdfoid on a Linux server, installing
> Segoe UI fonts on it will provide optimal rendering quality — otherwise, a fallback font will be used and
> statements will look subpar.

## Configuration

Configuring FreateOJ to generate PDFs with Pdfoid can be done by adding the following lines to your `local_settings.py`.

```python
# The URL Pdfoid is running on.
FREATEOJ_PDF_PDFOID_URL = 'http://localhost:8887'

# Optional, cache location for generated PDFs. You should consider using
# something more persistent than /tmp, since PDF generation is an expensive
# operation. If omitted, no cache will be used.
FREATEOJ_PDF_PROBLEM_CACHE = '/tmp'

# Optional, URL serving FREATEOJ_PDF_PROBLEM_CACHE with X-Accel-Redirect. This is
# recommended to have nginx serve PDFs, rather than uWSGI. To enable this,
# uncomment the line below, as well as the corresponding section in the sample
# nginx configuration file.
#FREATEOJ_PDF_PROBLEM_INTERNAL = '/pdfcache'
```

Restart FreateOJ for the changes to take effect.

## Troubleshooting

### "View as PDF" button doesn't show up

If a "View as PDF" button does not show up on the problem page, make sure that the `FREATEOJ_PDF_PDFOID_URL` variable is set.

### "View as PDF" button shows up

If a "View as PDF" button shows up, but generation fails, an error log should be displayed in the browser. This log will
also be captured by the `judge.problem.pdf` Django log handler. Depending on the error, explicitly setting the Pdfoid
environment variables `CHROME_PATH` to the path of the Chromium binary and `CHROMEDRIVER_PATH` to the path of the
ChromeDriver binary may alleviate the problem.

For other errors, take a look at the Selenium documentation,
specifically the common exceptions section.
