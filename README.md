# Receipt Processor

# Installation

This section guides you through the process of getting a copy of the source code, building the Docker image, and running the container using the provided Makefile.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Git
- Docker
- Make

## Cloning the Repository
To get started, clone the repository using Git:
```bash
git clone https://github.com/tayler20166/receipt-processor.git
cd receipt-processor
```

## Building the Docker Image
The project uses a Makefile to simplify Docker operations. To build the Docker image, run the following command:
```bash
make build
```
This command executes the build target in the Makefile, which is configured to build a Docker image using the Dockerfile found in the project directory.

## Running the Docker Container
Once the image is built, you can run the Docker container:
```bash
make run
```
This command executes the run target in the Makefile, which typically starts the Docker container with the appropriate configurations and port mappings specified in the Makefile.

## Verifying the Installation
After running the container, you can verify that it is up and running by checking the list of running containers:
```bash
docker ps
```

## Makefile Targets

The Makefile includes several targets for ease of use:

- `make build`: Builds the Docker image from the Dockerfile.
- `make run`: Runs the Docker container in detached mode.
- `make stop`: Stops the running Docker container if you need to halt the application.
- `make clean`: Removes the built Docker image and cleans up any resources that aren't in use anymore.


# Usage

This project includes a web application that exposes two RESTful endpoints to handle receipts and calculate points based on receipt content. Below you will find detailed instructions on how to use each endpoint.

## 1. Submitting Receipts for Processing

### Endpoint: `/receipts/process`

This endpoint accepts JSON formatted receipts and processes them to store receipt data.

**Method:** `POST`

**Request Body:**
- The request body should be JSON formatted and contain details of the purchase.
- Example:
```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}
```

**Response:**
- Returns a JSON object with the calculated points.
- Example:
```json
{ "id": "7fb1377b-b223-49d9-a31a-5a02701dd310" }
```


### Endpoint: `/receipts/{id}/points`

A simple Getter endpoint that looks up the receipt by the ID and returns an object specifying the points awarded.

**Response:**
```json
{ "points": 32 }
```


## Contact

If you have any questions or feedback, please contact me at artem.kamkov@gmail.com