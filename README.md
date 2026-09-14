# inverteer

Minimal `caliss` contact page with `name`, `number`, and `email` fields in `index.html`.

Open the repository's local `index.html` file in a browser to view the form.
When opened directly from disk, the page is view-only and submission is intentionally disabled.
The form submits the parameters `name`, `number`, and `email`.
To exercise submission locally, run `python server.py` from the repository root and open `http://127.0.0.1:8000/`.
When served from a web application, connect the relative `contact` form target to a backend that accepts `POST /contact`.
