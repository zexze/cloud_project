## Columbia University | 2024 Fall IEOR 4526 Cloud Analytic | Final Project
Team Members: Fan Bu (fb2635); Zexing Hu (zh2585)

URL: https://loanapprovalimg-560365338512.us-east4.run.app
Link Expires: 12/31/2024

### Run the program:
1. Build the image
```docker build -t loan-predictor .```
2. Start the container
```docker run -d -p 8080:8080 --name loan-predictor-container loan-predictor```
3. Access the container to check folder structure
```docker exec -it loan-predictor-container bash```
4. Stop the container
```docker stop loan-predictor-container```
5. Remove the container
```docker rm loan-predictor-container```



