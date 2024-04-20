// accessing form from the HTML page
form = document.getElementById('form'); 

// accessing the input elements from HTML page
const fullname = document.getElementById('id_full_name');
const phone = document.getElementById('id_phone_number');
const email = document.getElementById('id_email_id');
const dob = document.getElementById('id_dob');
const role = document.getElementById('id_job_role');
const gender = document.getElementById('id_gender');

// accessing fields which shows error messages in HTML page
const error_fname = document.getElementById('error-fname');
const error_phone = document.getElementById('error-phone');
const error_email = document.getElementById('error-email');
const error_dob = document.getElementById('error-dob');
const error_role = document.getElementById('error-role');
const error_gender = document.getElementById('error-gender');

// event listener which triggers on submission of form
// will check for validation errors for the mentioned fields
form.addEventListener('submit', function(event) {
    validateFullName(event);
    validatePhoneNumber(event);
    validateEmail(event);
    validateDob(event);
    validateJobRole(event);
    validateGender(event);
});

// function to validate full name
function validateFullName(event){
    
    let messages = []  // array to store error messages
    const fullNameRegex = /^[a-zA-Z ]+$/ 
    
    if (fullname.value === '' || fullname.value == null){
        messages.push('Name cannot be empty')
        window.scrollTo(0,0)  // move to top op the page if an error is found
    } 
    else if (!fullNameRegex.test(fullname.value)) {
        messages.push('Error in full name')
        window.scrollTo(0,0)
    } 
    else if (fullname.value.length < 3){
        messages.push('Minimum 3 characters required')
        window.scrollTo(0,0)
    }
    else if (fullname.value.length > 75){
        messages.push('Maximum 75 characters allowed')
        window.scrollTo(0,0)
    }
    else {
        error_fname.innerText = messages.join(', ');
    }
    
    // checks for error present in the input
    if (messages.length > 0) {
        event.preventDefault();  // prevent the submission of the form
        error_fname.innerText = messages.join(', ');  // display the error message
    }    
}

// event listener perfoming the validations on change
form.addEventListener('change', (event) => {
    validateFullName(event); 
});


// function to validate phone number
function validatePhoneNumber(event) {
    let messages = []
    const phoneRegex = /^\d{10}$/

    if(phone.value === ''|| phone.value == null) {
        messages.push('Phone number cannot be empty')
        window.scrollTo(0,0)
    } 
    else if (!phoneRegex.test(phone.value)){
        messages.push('Invalid phone number')
        window.scrollTo(0,0)
    } 
    else {
        error_phone.innerText = messages.join(', ')   
    }
    
    if (messages.length > 0) {
        event.preventDefault();
        error_phone.innerText = messages.join(', ')
    }
}

// event listener perfoming the validations on change
form.addEventListener('change', (event) => {
    validatePhoneNumber(event);
});

// function to validate email
function validateEmail(event) {
    let messages = []
    const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

    if(email.value === '' || email.value == null) {
        messages.push('Email ID cannot be empty')
        window.scrollTo(0,0)
    }
    else if (!emailRegex.test(email.value)) {
        messages.push('Invalid Email ID')
        window.scrollTo(0,0)
    }
     else {
        error_email.innerText = messages.join(', ')
    }
    
    if (messages.length > 0) {
        event.preventDefault();
        error_email.innerText = messages.join(', ')
    }
}

// event listener perfoming the validations on change
form.addEventListener('change', (event) => {
    validateEmail(event);
});

//  function to validate DOB
// allows only applicants with minimu  age of 18 years
function validateDob(event) {
    const currDate = new Date(); // get current date
    const year = currDate.getFullYear();
    const month = String(currDate.getMonth() +1).padStart(2, '0');
    const day = String(currDate.getDate()).padStart(2, '0');
    const today = `${year}-${month}-${day}`;  // current date

    const givenDate = dob.value;      // the date from input 'date' field
    
    const date1 = new Date(today);
    const date2 = new Date(givenDate);
    const timeDiff = Math.floor((date1-date2)/(1000*60*60*24*365.25)); // calculating the age
    let messages = []

    if (timeDiff < 18) {
        messages.push('Invalid Date of Birth, applicant must be minimum 18 years old')
        window.scrollTo(0,0)
    } 
    else if (dob.value === '' || dob.value == null){
        messages.push('DOB cannot be empty')
        window.scrollTo(0,0)
    }
    else {
        error_dob.innerText = messages.join(', ')
    }
    if (messages.length > 0) {
        event.preventDefault();
        error_dob.innerText = messages.join(', ')
    }
}

// event listener perfoming the validations on change
form.addEventListener('change', (event) => {
    validateDob(event);
});

// function to validate Job Role
function validateJobRole(event){
    let messages = []
    if (role.value == "" || role.value == null){
     messages.push('Please select a role from the given options')
    }
    else {
     error_role.innerText = messages.join(', ')
    }
    if (messages.length > 0) {
     event.preventDefault();
     error_role.innerText = messages.join(', ')
     }
 }
 
 // event listener perfoming the validations on change
 form.addEventListener('change', (event) => {
     validateJobRole(event);
 });
 
function validateGender(event) {
    var flag = false;
    let messages = []
    for (var val = 0; val < gender.length; val++){
        if(gender[val].checked) {
            flag = true
            break;
        }
        else if (flag == false){
            messages.push('Gender cannot be empty. Select one option from above');
            error_gender.innerText = messages.join(', ');
        }
        if(messages.length > 0) {
            event.preventDefault();
            error_gender.innerText = messages.join(', ');
        }
    }

 }

 // event listener perfoming the validations on change
form.addEventListener('change', (event) => {
    validateGender(event);
});

// prevent the page navigation to previous page
function preventbackbutton(){window.history.forward();}
setTimeout("preventbackbutton()", 0);
window.onunload=function(){null};
 