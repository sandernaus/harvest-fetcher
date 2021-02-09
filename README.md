# harvest-fetcher

Tool to fetch registered time entries from your harvest account and store in DB.

A userid and token are required to use the API. This information can be created in the [developers section](https://id.getharvest.com/developers) of the harvest account

## Dependencies

```bash
pip install -r requirements.txt
```

## Execute

```bash
python fetch_time.py
```

## .secret.yml

User ID and Token are proved through a `.secret.yml` file:

```yaml
---
userid: UserID123
token: Token123
```
