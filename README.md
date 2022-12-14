# LocalStack Hackmas Demo 2022

- Run the cookie cutter:
  ```
  cookiecutter --no-input --config-file config.yaml git@github.com:alexrashed/cookiecutter-ls-oa-ext.git
  ```
- Inspect the result!
  - We generated a new python project.
  - We used OpenAPI Generator to generate an API stub based on an API spec.
    - It used [`connexion`](https://github.com/spec-first/connexion) to serve the API.
    - `connexion` is based on `flask`!
    - `flask` is based on `werkzeug`!
    - `werkzeug` is the base for our new gateway!
  - The generated code directly integrates with our router (instead of serving a flask app on another port and forwarding the requests)!
- Run LocalStack with the extension:
  ```
  localstack login
  localstack extensions init
  localstack extensions dev enable ./localstack-christmas-countdown/
  DEBUG=1 EXTENSION_DEV_MODE=1 DNS_ADDRESS=127.0.0.1 LOCALSTACK_API_KEY="..." localstack start
  ```
- Checkout the API!
  ```
  curl https://localhost.localstack.cloud/timeleft/total
  ```
- Add our implementation:
  ```
  cp code/* localstack-christmas-countdown/localstack_christmas_countdown/controllers
  ```
- Restart LocalStack
  ```
  curl "https://localhost.localstack.cloud/timeleft/total?timezone=America/New_York"
  ```