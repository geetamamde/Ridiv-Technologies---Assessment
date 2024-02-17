
#  Ridiv Technologies - Assessment

You need to create a single url /invoices/ for thisCreate a Django application (Django Rest Framework) using the given information: You need to create a single url /invoices/ for this /invoices/ /invoices// - Create two Django models viz. Invoice and Invoice Detail. - Invoice model fields -> Date, Invoice CustomerName. - InvoiceDetail model fields -> invoice (ForeignKey), description, quantity, unit_price, price. - Create APIs using Django Rest Framework for all the HTTP methods for the invoice models. - The API should also accept invoice_details in the payload and create/update the associated invoice details too - Create test cases to test all the API endpoints.


## Installation

Clone the repository from GitHub:

```bash
  https://github.com/geetamamde/Ridiv-Technologies---Assessment.git

  cd Ridiv-Technologies---Assessment
```
Run the database migrations :

```bash
 python manage.py migrate
```
To start the Django development server, run the following command:
  
```bash
 python manage.py runserver
```  
## API Endpoints

The application provides the following API endpoints:

GET: Retrieve details of a specific invoice.

/invoices/Invoice//{invoice_id}


![GET](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/103e013b-0e4f-44be-a2aa-f21339e28f38)

/invoices/InvoiceDetailViewSet//

![invoiceDetailGet](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/bbd1435f-b628-4c25-8bd8-c6e317d209a3)

POST: Create a new invoice
/invoices/Invoice//
![POST](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/c45a89a9-1f45-40ad-afe6-dbb09f318f8d)

/invoices/InvoiceDetailViewSet//
![invoiceDetailsPOST](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/b345f130-3360-4f46-a553-9f2cf9c6819b)


PUT: Update details of a specific invoice.
/invoices/Invoice//{invoice_id}
![PUT](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/c6787457-5103-4a3e-b131-3150dc3fe067)

/invoices/InvoiceDetailViewSet//{invoice_id}

![invoice Details PUT](https://github.com/geetamamde/Ridiv-Technologies---Assessment/assets/105689568/d4a4fbf1-6d9b-4ba1-8f6b-69041d4f6e8d)
