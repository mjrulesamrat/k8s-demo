# Bank of Spain Service

Palermo makes REST API calls over HTTP 2.0 to Professor service with the latest updates from the Bank of Spain

## Running guidelines

- Install Dependencies

    ```
    pip install fastapi

    pip install 'uvicorn[standard]'
    ```

- Run server with below command

    ```
    uvicorn run:app --reload
    ```

- Testing Application locally

    ```
    docker build -t bank-service:latest .
    docker images  # list down images
    docker run -p 8082:8082 bank-service:latest  # host-port:container-port
    ```