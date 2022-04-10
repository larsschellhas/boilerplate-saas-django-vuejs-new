# Software-as-a-Service boilerplate using Django and Vue.JS
This repository contains a boilerplate setup for a software-as-a-service app, using Django for the backend and Vue.JS for the frontend.

## Features
### Backend
- Django + Django Rest Framework
- User management via Auth0.com
- Payment & subscription management via Paddle.com


### Frontend
- Vue.JS 3 with fully Composition API based Components
- Abstract API service layer fully configured for backend
- Persisted central state with Vuex
- Localization with vue-i18n
    - browser language is detected on first visit
    - language selected by user is persisted in vuex store
    - locale messages are lazyloaded

## Development setup
You need to have the following prerequisites installed:
- Python 3.10
- Poetry [(Installation Guide)](https://python-poetry.org/docs/master/#installation)
- Node.js 16[(Installation Guide)](https://nodejs.dev/learn/how-to-install-nodejs)
- Yarn [(Installation Guide)](https://yarnpkg.com/getting-started/install#about-global-installs)
- Docker Desktop [(Download)](https://www.docker.com/products/docker-desktop)
- pre-commit [(Installation Guide)](https://pre-commit.com/#install)
- Visual Studio Code [(Download)](https://code.visualstudio.com/Download)
- Workspace Recommended Visual Studio Code Extensions
    - Go to the extensions tab (Ctrl + Shift + X)
    - Type `@recommended` in the search bar
    - Install all shown workspace recommendations

Following the installation of all required toosl, follow these steps to finish the setup of your development environment:
1. Install all python dependencies in a virtual environment via poetry by running `poetry install` in the `.\backend` directory
2. Install all JS dependencies via yarn by running `yarn install` in the `.\frontend` directory
3. Install the pre-commit hooks to profit from automatic recreation of Python's requirements files by running `pre-commit install` in the root project directory.
    
4. Create a basic development configuration 
    1. Copy the file '.env.development.template' and rename the copy to '.env.development'
    2. Set `DJANGO_SECRET_KEY` to a random string, e.g., by using this [secret key generator (Link)](https://django-secret-key-generator.netlify.app/)
    3. Set `ADMIN_EMAIL` to your email (or any) and `ADMIN_PASSWORD`to a password of your choice. These credentials can later be used to log into the Django admin dashboard, independently from the authentication provider (Auth0).
    4. Set all entries starting with `EMAIL_XXX` to configure your e-mail backend. Alternatively, delete any or all of these entries and Django will automaticaly output any sent emails to the console instead of sending actual emails.

5. Setup Auth0
    1. Create an Auth0 account [here (auth0.com)](https://auth0.com/signup?place=header&type=button&text=sign%20up) and choose an 'auth0 domain' suiting the name of your app or business.
    In your `.env.development`file, add your chosen 'Auth0 domain' to the `VUE_APP_AUTH0_DOMAIN` entry.
    Your account (or rather the tenant you created) is being setup as development tenant automatically. Splitting your production and development tenant makes sense for external services, too. We will switch to production later, after deploying our SaaS.
    2. Create an Auth0 API [here](https://manage.auth0.com/#/apis) and add your chosen 'Identifier' (e.g., 'https://django-vuejs-api') to the `VUE_APP_AUTH0_API_IDENTIFIER` entry in your `.env.development`file.
    For example, you could use this data:
        - Name: Django Vue.js API
        - Identifier: https://django-vuejs-api
        - Signing Algorithm: RS256
    3. Go to ["Applications"](https://manage.auth0.com/#/applications) to create a new application. 
        - Click on the button "+ Create Application", give your application a meaningful name and select "Single Page Web Application". Then, click "Create".
        - You will be forwarded to the details page of your new Auth0 application. Copy the "Client ID" of your application, which you can find directly below the big title/name of your app. In your `.env.development`file, add your copied 'Client ID' to the `VUE_APP_AUTH0_CLIENT_ID` entry.

6. Setup Paddle
    1. Create a Paddle account on their [development/sandbox server (signup)](https://sandbox-vendors.paddle.com/signup). This will allow you to try out all paddle features without the fear of messing anything up.
    2. Go to [Developer Tools > Authentication](https://sandbox-vendors.paddle.com/authentication)
        - Copy your 'vendor_id' from the top of the page. In your `.env.development`file, add your copied 'vendor_id' to the `VUE_APP_PADDLE_VENDOR` entry.
        - Create a new API auth code through the "Generate Auth Code" form on the page. Your new API will appear in the list of "Active Integrations & Auth Codes".
        - Click on the "Reveal Auth Code" button on the right to your new API and copy the appeared auth code. In your `.env.development`file, add your copied auth code to the `PADDLE_API_KEY` entry.
    3. Go to [Developer Tools > Public Key](https://sandbox-vendors.paddle.com/public-key) and copy the displayed public key.
    In your `.env.development`file, add your copied 'vendor_id' to the `PADDLE_PUBLIC_KEY` entry.

7. Build all docker images and run the application with the following command:
`docker-compose -f docker-compose.development.yml up --build`. 
This will use the development configuration for docker and allow you to test your application for the first time at [localhost](http://localhost).


#### Environmental variables
Many crucial settings are set through environmental variables to keep them out of the code repository.
If the environmental variable `VUE_APP_PRODUCTION` is not set to `True`, the development configuration is used which is read from `.env.development`. All environmental variables that need to be set are present in the file `.env.default.template`.

Some environmental variables are prefixed by `VUE_APP_`. This is required for accessing environmental variables in the frontend Vue.js app. However, some variables are only used for the backend and should never be available in the frontend. These variables **do not have** the `VUE_APP_` prefix and should never have it to avoid potential data leakage on the frontend.

##### Development setup
For development purposes, it is enough to copy the template file, rename it to `.env.development`, and change the values of all settings accordingly.
##### Production setup
For your production setup, you should set all of the environmental variables in your server settings and set `VUE_APP_PRODUCTION` to `True`. Some cloud providers might automatically add `WEBSITE_HOSTNAME` or other environmental variables.


### Troubleshooting

#### `poetry install` fails with `No module named 'virtualenv.seed.via_app_data'` on Linux/WSL

In this case, following [this comment on GitHub](https://github.com/python-poetry/poetry/issues/2972#issuecomment-717563513), you need to uninstall the Python package `virtualenv` with Linux's `apt` command:
```
sudo apt remove --purge python3-virtualenv virtualenv
```

Afterwards, you can reinstall it using `pip3`:
```
pip3 install virtualenv
```

#### wrong local python3 version
Instead of changing it you can run all rommands with `python3.10` instead of `python`

#### `yarn install` fails with `No such file or directory: 'install'` on Linux/WSL
Solution: https://stackoverflow.com/questions/46013544/yarn-install-command-error-no-such-file-or-directory-install

```
sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn -y
```
