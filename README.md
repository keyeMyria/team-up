# Team-up server repository


## Useful links
[Slack](https://team-up--hq.slack.com)

[trello](https://trello.com/team_up1)

## Style guidelines
* Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) for Python code.

* Try to keep line width under 120 characters.

* Use [formatted string literals](https://www.python.org/dev/peps/pep-0498/) for string formatting.

* Use [Type Hints](https://www.python.org/dev/peps/pep-0484/) whenever possible.

* For docstrings in everything but views use [google style docstring.](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

* Code for the API endpoints should be places in `api` folder, except of the `search` endpoint.

* Names, variables, docstring, comments, etc. should be written in english.

* Test files should be placed in `tests` dir in directory where tested file is.

## Workflow
1. Pick ticket from `TODO` list on [workboard](https://trello.com/b/48D3VAPK/workboard).
2. Move it to `In progress` list and change it to your color.
3. Create git branch with name in the following format `<ticket_id>-<descriptive_name>`.
4. Do the ticket.
5. Remember to run all tests.
6. When finished create pull request to master and ask another team member for code review.
7. Wait for branch to be merged.
    * If you are the one who merges remember to use `squach and merge` option and to delete the branch after merging.

## Makefile
There is a Makefile with following commands:

* `build-all` - Build all containers, dev-build by default:
    * `build-redis`
    * `build-postgres`
    * `build-django`
    * `build-nginx`
* `rebuild-all` - Remove all containers and volumes and rebuilds them:
    * `rebuild-redis`
    * `rebuild-postgres`
    * `rebuild-django`
    * `rebuild-nginx`
* `run-dev` - Run containers in development mode
* `run-dev-no-logs` - Run containers in development mode without output to the console
* `migrate` - Run migrations in flask container
* `stop` - Stop all containers:
    * `stop-redis`
    * `stop-postgres`
    * `stop-django`
    * `stop-nginx`
* `rm` - Remove all containers:
    * `rm-redis`
    * `rm-postgres`
    * `rm-django`
    * `rm-nginx`
* `rm-all-volumes` - Remove all volumes:
    * `rm-db-volume`
    * `rm-nginx-volume`
* `clean-all` - Stop and remove all containers and volumes:
    * `clean-redis`
    * `clean-postgres`
    * `clean-django`
    * `clean-nginx`
* `shell-redis` - Open Bash shell in redis container
* `shell-postgres` - Open Bash shell in postgres container
* `shell-django` - Open Bash shell in django container
* `shell-nginx` - Open Bash shell in nginx container
* `logs` - Output all logs to the terminal:
    * `logs-redis`
    * `logs-postgres`
    * `logs-django`
    * `logs-nginx`
* `dev-reload` - Watch files for changes and reloads services when needed.
* `reload-nginx` - Reload nginx
* `prepare-tests` - Start containers in test mode
* `test` - Run tests inside containers.
