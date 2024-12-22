# telegram-bot-proxy
Very basic `Telegram` user-bot to mirror messages from multiple sources to multiple destinations.

Since telegram bots can't read each others messages, you are required to create an API ID and HASH for your(or a random)
account, to use with this setup, following the official docs: https://core.telegram.org/api/obtaining_api_id#obtaining-api-id

After you obtained your key, you can configure the proxy by simply editting the Makefile with your config options:
| Config         | Description                                             |
|----------------|---------------------------------------------------------|
| `API_ID`       | Your API key, provided by `telegram`                    |
| `API_HASH`     | Your API hash, provided by `telegram`                   |
| `PHONE`        | Your `telegram` account phone number                    |
| `DB_PASS`      | Password used to encrypt the account information        |
| `DEST_GROUPS`  | The `tg` groups you want to mirror/forward the messages |
| `BOTS_GROUP_ID`| The `tg` groups you want to source messages from        |

## Usage
Script provides the following Make targets:
| Target      | Description                             |
|-------------|-----------------------------------------|
| `bootstrap` | Create the environment and get all deps |
| `clean`     | Remove build artifacts                  |
| `deploy`    | Start the proxy using the configuration |

### Environment setup
The following OS dependencies are required:
|   Dependency   |
|----------------|
| git            |
| make           |
| python         |
| python-venv    |
| libssl1.1      |

Before first usage, you have to grab all the required python libraries:
```
% make bootstrap
```
### Execution
Since we are using a `python` virtual environment, we have to source
it before starting the proxy:
```
% . {FULL_PATH_REPO}/venv/bin/activate
```
After that, you can modify the configuration and start the proxy:
```
% make deploy
```
After the mirror is up and running, you can verify it's working by
waitting to see if messages from source groups are forwarded to the
destination groups.
