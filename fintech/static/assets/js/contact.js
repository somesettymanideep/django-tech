// $(document).ready(function() {
//   $('#submit-btn').click(function() {
//       let formData = new FormData();
//       debugger
//       formData.append('Company Name', $('#company-name').val());
//       formData.append('Business Type', $('input[name="Business Type"]:checked').val());
//       formData.append('Years in Business', $('#years-in-business').val());
//       formData.append('Company Insured', $('input[name="Company Insured"]:checked').val());
//       formData.append('Company Licensed', $('input[name="Company Licensed"]:checked').val());
//       formData.append('GST Number', $('#gst-number').val());
//       formData.append('Products Services', $('#products-services').val());
//       formData.append('Company Website', $('#company-website').val());
//       formData.append('Company Address', $('#company-address').val());
//       formData.append('City', $('#city').val());
//       formData.append('State', $('#state').val());
//       formData.append('Postal Code', $('#postal-code').val());
//       formData.append('Country', $('#country').val());
//       formData.append('Company Year', $('#company-year').val());
//       formData.append('First Name', $('#first-name').val());
//       formData.append('Last Name', $('#last-name').val());
//       formData.append('Country Code', $('#country-code').val());
//       formData.append('Phone Number', $('#phone-number').val());
//       formData.append('Email', $('#email').val());
      
//       $.ajax({
//           type: 'POST',
//           url: '/contact/',
//           processData: false,
//           contentType: false,
//           cache: false,
//           data: formData,
//           success: function(data, status, xhr) {
//               $('#contact-form')[0].reset();
//               if(data.success === true){
//                   alert("Form Submission Successful");
//               } else {
//                   alert("Invalid Form Submission");
//               }   
//           },
//           error: function(data) {
//               alert("Form Submission Failed");
//           }
//       });
//   });
// });
$(document).ready(function(){
  $('#submit-btn').click(function(event){
      event.preventDefault(); // Prevent the default form submission

      let companyName = $('input[name="Company Name"]').val();
      let businessType = $('input[name="Business Type"]:checked').val();
      let yearsInBusiness = $('input[name="Years in Business"]').val();
      let companyInsured = $('input[name="Company Insured"]:checked').val();
      let companyLicensed = $('input[name="Company Licensed"]:checked').val();
      let gstNumber = $('input[name="GST Number"]').val();
      let productsServices = $('textarea[name="Products Services"]').val();
      let companyWebsite = $('input[name="Company Website"]').val();
      let companyAddress = $('input[name="Company Address"]').val();
      let city = $('input[name="City"]').val();
      let state = $('input[name="State"]').val();
      let postalCode = $('input[name="Postal Code"]').val();
      let country = $('select[name="Country"]').val();
      let companyYear = $('input[name="Company Year"]').val();
      let firstName = $('input[name="First Name"]').val();
      let lastName = $('input[name="Last Name"]').val();
      let countryCode = $('select[name="Country Code"]').val();
      let phoneNumber = $('input[name="Phone Number"]').val();
      let email = $('input[name="Email"]').val();
      let csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val(); // Get CSRF token

      let data = new FormData();
      data.append('Company Name', companyName);
      data.append('Business Type', businessType);
      data.append('Years in Business', yearsInBusiness);
      data.append('Company Insured', companyInsured);
      data.append('Company Licensed', companyLicensed);
      data.append('GST Number', gstNumber);
      data.append('Products Services', productsServices);
      data.append('Company Website', companyWebsite);
      data.append('Company Address', companyAddress);
      data.append('City', city);
      data.append('State', state);
      data.append('Postal Code', postalCode);
      data.append('Country', country);
      data.append('Company Year', companyYear);
      data.append('First Name', firstName);
      data.append('Last Name', lastName);
      data.append('Country Code', countryCode);
      data.append('Phone Number', phoneNumber);
      data.append('Email', email);
      data.append('csrfmiddlewaretoken', csrfmiddlewaretoken); // Append CSRF token

      $.ajax({
          type: 'POST',
          url: '/contactus/',
          processData: false,
          contentType: false,
          cache: false,
          data: data,
          success: function(response){
              if(response.success === true){
                  alert("Form Submission Successful");
                  $('#contact-form')[0].reset();
              } else {
                  alert("Invalid Form Submission: " + response.error);
              }   
          },
          error: function(xhr){
              let errorMessage = xhr.status + ': ' + xhr.statusText;
              alert("Form Submission Failed: " + errorMessage);
          }
      });
  });
});

$(document).ready(function() {
    $('#reach-btn').click(function(event) {
        event.preventDefault(); // Prevent the default form submission
        debugger
        let fullName = $('input[name="Full Name"]').val();
        let emailAddress = $('input[name="Email Address"]').val();
        let phoneNo = $('input[name="Phone No"]').val();
        let message = $('textarea[name="msg"]').val();
        let csrfToken = $('[name=csrfmiddlewaretoken]').val(); 

        let data = new FormData();
        data.append('Full Name', fullName);
        data.append('Email Address', emailAddress);
        data.append('Phone No', phoneNo);
        data.append('msg', message);
        data.append('csrfmiddlewaretoken', csrfToken); // Append CSRF token

        $.ajax({
            type: 'POST',
            url: '/reachus/',
            processData: false,
            contentType: false,
            cache: false,
            data: data,
            success: function(response) {
                if (response.success === true) {
                    alert("Form Submission Successful");
                    $('#reach-form')[0].reset();
                } else {
                    alert("Invalid Form Submission: " + response.error);
                }
            },
            error: function(xhr) {
                let errorMessage = xhr.status + ': ' + xhr.statusText;
                alert("Form Submission Failed: " + errorMessage);
            }
        });
    });
});
