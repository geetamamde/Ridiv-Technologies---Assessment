
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
/invoices/Invoice//
/invoices/InvoiceDetailViewSet//

POST: Create a new invoice
/invoices/Invoice//
/invoices/InvoiceDetailViewSet//

PUT: Update details of a specific invoice.
/invoices/Invoice//{invoice_id}
/invoices/InvoiceDetailViewSet//{invoice_id}

