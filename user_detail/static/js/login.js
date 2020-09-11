function loginValidate()
{
  var email_id = document.forms["login"]["email_id"].value;
  if(email_id.trim().length === 0)
  {
    alert("Email ID should not be empty");
    return false;
  }
  else
  {
    var password = document.forms['login']['password'].value;
    if(password.trim().length === 0)
    {
      alert('Password should not be empty');
      return false;
    }
  }
}