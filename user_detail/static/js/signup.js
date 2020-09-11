function formValidate()
{
  var username = document.forms["signup"]["username"].value;
  if(username.trim().length === 0)
  {
    alert("Username should not be empty");
    return false;
  }
  else
  {
    var email = document.forms['signup']['email_id'].value;
    var reg = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    if(email.trim().length === 0)
    {
      alert('Email ID should not be empty');
      return false;
    }
    else if (!reg.test(email))
    {
      alert("Please Enter Valid Email Address");
      return false;
    }
    else
    {
      var password = document.forms['signup']['password'].value;
      if(password.trim().length === 0)
      {
        alert('Password should not be empty');
        return false;
      }
      else if(password.trim().length<8)
      {
        alert('Password should not be less than 8 characters');
        return false;
      }
      else if(password.trim().length>20)
      {
        alert('Password should be less than 20 characters');
        return false;
      }
      else
      {
        var password = document.forms['signup']['password'].value
        var confirm_password = document.forms['signup']['confirm_password'].value;
        if(confirm_password.trim().length === 0)
        {
          alert('Confirm Password should not be empty');
          return false;
        }
        else if(password.trim() != confirm_password.trim())
        {
          alert('Password and Confirm Password is mismatching...');
          return false;
        }
      }
    }
  }
}
          