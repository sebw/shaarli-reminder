# Shaarli bookmark reminder

If you use Shaarli and want to be reminded to check some links in the future (for example a product that would launch, some progress on a Github repository), you just need to tag a link with something like `remindme202209`.

`202209` means you'd want to check that website again in September 2022.

Now you just need to run this container (see below) on the 1st of each month (or really once any day of the month). When run, the container will find links tagged with `remindme202209` and it will send a summary.

You have two ways to run this container.

## Running the pre-built container 

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
  ghcr.io/sebw/shaarli-reminder:v0.0.1
```

Anytime you run the container, you will receive the summary by email.

## Building and running the container locally

```
git clone https://github.com/sebw/shaarli-reminder.git
cd  shaarli-reminder
podman build -t shaarli-reminder:v0.0.1
```

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
  shaarli-reminder:v0.0.1
```
