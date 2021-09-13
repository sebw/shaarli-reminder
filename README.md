# Shaarli bookmark reminder

If you use Shaarli and want to be reminded to check some links in the future (for example a product that would launch, some progress on a Github repository), you just need to tag a link with something like "remindme202209".

202209 means you want to check that website again in September 2022.

This container can be run from a cron job on the first of each month with:

```
podman run \
  -e SHAARLI_URL=https://shaarli.example.org \
  -e SHAARLI_API=your_api_token \
  -e SHAARLI_TAG=remindme`date +%Y%m` \
  -e SMTP_USERNAME=user@example.org \
  -e SMTP_SENDER=user@example.org \
  -e SMTP_RECIPIENT=recipient@example.org \
  -e SMTP_PASSWORD=your_email_password \
  -e SMTP_SERVER=smtp.example.com \
  -e SMTP_PORT=587 \
  --name=shaarli-reminder \
  sebastienw/shaarli-reminder:v0.0.1
```

You will receive a summary by email.
