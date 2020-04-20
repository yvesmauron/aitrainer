# Aitrainer 1.0


# how to develop

During local development

```{Python}
if __name__ == '__main__':
    app.run_server(debug=True)
```

local test with gunicorn

```{bash}
gunicorn app:server -b localhost:8080
```