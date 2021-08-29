# Professor Service

Professor mostly listens to the requests coming from Bank of Spain and sometimes calls back the bank service for next action plans.

For each request coming from the Bank, Professor sends one socket event to Marseille, to keep Police engaged in his Genius Plan.

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
