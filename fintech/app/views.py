from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from .models import ContactSubmission


# Create your views here.
def index(request):
    return render(request, 'uifiles/index.html')


@csrf_exempt
def reachus(request):
    if request.method == 'POST':
        full_name = request.POST.get('Full Name')
        email_address = request.POST.get('Email Address')
        phone_no = request.POST.get('Phone No')
        message = request.POST.get('msg')

        if full_name and email_address and phone_no and message:
            # Save the submission to the database
            submission = ContactSubmission(
                full_name=full_name,
                email_address=email_address,
                phone_no=phone_no,
                message=message
            )
            submission.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'All fields are required.'})
    elif request.method == 'GET':
        return render(request, 'uifiles/reachus.html')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})



@csrf_exempt
def contactus(request):
    if request.method == 'POST':
        company_name = request.POST.get('Company Name')
        business_type = request.POST.get('Business Type')
        years_in_business = request.POST.get('Years in Business')
        company_insured = request.POST.get('Company Insured') == 'Yes'
        company_licensed = request.POST.get('Company Licensed') == 'Yes'
        print(company_insured,company_licensed)
        gst_number = request.POST.get('GST Number')
        products_services = request.POST.get('Products Services')
        company_website = request.POST.get('Company Website')
        company_address = request.POST.get('Company Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        postal_code = request.POST.get('Postal Code')
        country = request.POST.get('Country')
        company_year = request.POST.get('Company Year')
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        country_code = request.POST.get('Country Code')
        phone_number = request.POST.get('Phone Number')
        email = request.POST.get('Email')

        # Example validation
        if not company_name or not email:
            return JsonResponse({'success': False, 'error': 'Company Name and Email are required fields.'})

        # Save to database
        contact = Contact(
            company_name=company_name,
            business_type=business_type,
            years_in_business=years_in_business,
            company_insured=company_insured,
            company_licensed=company_licensed,
            gst_number=gst_number,
            products_services=products_services,
            company_website=company_website,
            company_address=company_address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            company_year=company_year,
            first_name=first_name,
            last_name=last_name,
            country_code=country_code,
            phone_number=phone_number,
            email=email
            
        )
        contact.save()
        
        

        # Return success response
        return JsonResponse({'success': True})

    # For GET requests, render the contact form page
    return render(request, 'uifiles/contact.html')
