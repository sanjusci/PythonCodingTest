# PythonCodingTest

### Coding exercise:

##### Write a Flask Web API with only 1 method called `ProcessPayment` that receives a request like this

    -CreditCardNumber (mandatory, string, it should be a valid credit card number)
    -CardHolder: (mandatory, string)
    -ExpirationDate (mandatory, DateTime, it cannot be in the past)
    -SecurityCode (optional, string, 3 digits)
    -Amount (mandatoy decimal, positive amount)
    

#####The response of this method should be 1 of the followings based on

    -Payment is processed: 200 OK
    -The request is invalid: 400 bad request
    -Any error: 500 internal server error
    
#####The payment could be processed using different payment providers (external services)called:

    -PremiumPaymentGateway
    -ExpensivePaymentGateway
    -CheapPaymentGateway.

##### The payment gateway that should be used to process each payment follows the next set of business rules:

    a)If the amount to be paid is less than £20, use CheapPaymentGateway.
    b)If the amount to be paid is £21-500, use ExpensivePaymentGateway if available. Otherwise, retry only once with CheapPaymentGateway.
    c)If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times in case payment does not get processed.
    

## Prerequisites

- [Python](https://www.python.org/downloads/) >= 3.6
- [Pip3](https://pypi.python.org/pypi/pip) >= 1.5
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)>= 1.11

### Setup & Installation

- Create virtual environment, and activate it (Optional)-

```bash
# Install `virtualenv`
virtualenv -p python3 .env

# Activate virtual environment
source .env/bin/activate
```

- Clone git repository -

```bash
git clone https://github.com/sanjusci/PythonCodingTest.git

# cd to `project-dir`
cd smartview_flask
```

- Install dependencies -

    On Local -
    
    ```bash
    pip3 install -r requirements.txt
    ```
    On Prod - 
    
    ```bash
    pip3 install -r requirements.txt --user
    ```

```bash
# Add current project to `PYTHONPATH`
export PYTHONPATH="$PYTHONPATH:."
```

- Set environment variables -

> If project is being run under `virtualenv` then environment variables can be set under `.env/bin/activate` file.

```bash
vim .env/bin/activate

# Append following lines at the end of the file after making appropriate changes.
export FLASK_APP=app
```

### Running Application
```
> flask run

```
 
### How to test the application
 
   1. Run the server application server using above commands
   2. Activate virtual environment
   3. in separate terminal, run `cd test` ie go to test folder
   4. run commands: `pytest test_creditcard_unittest.py` or
   5. run commands: `tox`
   
