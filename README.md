# Hugging Face Api Proxy
Proxies requests to HF while hiding the API token

To run locally

```bash
export HF_TOKEN=...
poetry run uvicorn hugging_face_api_proxy:app
```

To run locally in docker using 

```bash
# you need to install pack (https://buildpacks.io/docs/tools/pack/)
pack build --builder tools-harbor.wmcloud.org/toolforge/heroku-builder:22 hf_api_proxy
docker run -e PORT=8000 -e HF_TOKEN=... -p 8000:8000 --rm --entrypoint web hf_api_proxy
```

To deploy on toolforge run

```bash
become mytool
toolforge envvars create HF_TOKEN
toolforge build start https://github...
toolforge webservice --backend=kubernetes --mount=none buildservice start
```
