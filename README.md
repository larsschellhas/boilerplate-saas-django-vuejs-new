# SimplyLCA-App
This repository is for the development of our app.

## Local Setup

You need to have the following prerequisites installed:
- Python 3.8
- Poetry [(Installation Guide)](https://python-poetry.org/docs/#installation)
- Node.js
- Yarn [(Installation Guide)](https://yarnpkg.com/getting-started/install#about-global-installs)
- Visual Studio Code [(Download)](https://code.visualstudio.com/Download)
- Workspace Recommended Visual Studio Code Extensions
    - Go to the extensions tab (Ctrl + Shift + X)
    - Type `@recommended` in the search bar
    - Install all shown workspace recommendations



### Backend project
1. Enter the backend project directory (e.g. SimplyLCA-App/backend)
2. Install all dependencies via poetry by running `poetry install`
3. Activate the virtual Python environment created by poetry with `poetry shell`
4. Setup/migrate the database server with `python manage.py migrate`
5. Run the webserver with `python manage.py runserver`

### Frontend project
1. Enter the frontend project directory (e.g. SimplyLCA/frontend)
2. Install all dependencies with `yarn install`
3. Run the webserver with `yarn serve`

### Troubleshooting

#### `poetry install` fails with `No module named 'virtualenv.seed.via_app_data'`

In this case, following [this comment on GitHub](https://github.com/python-poetry/poetry/issues/2972#issuecomment-717563513), you need to uninstall the Python package `virtualenv` with Linux's `apt` command:
```
sudo apt remove --purge python3-virtualenv virtualenv
```

Afterwards, you can reinstall it using `pip3`:
```
pip3 install virtualenv
```

#### `poetry install` fails with `poetry: command not found`
```
source $HOME/.poetry/env
```

#### wrong local python3 version
Instead of changing it you can run all rommands with `python3.8` instead of `python`

#### `yarn install` fails with `No such file or directory: 'install'`
Solution: https://stackoverflow.com/questions/46013544/yarn-install-command-error-no-such-file-or-directory-install

```
sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn -y
```
