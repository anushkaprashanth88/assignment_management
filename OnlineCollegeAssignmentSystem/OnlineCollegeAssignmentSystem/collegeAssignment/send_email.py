from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from .models import *

SENDEREMAIL = "adhwaithaprashanth2003@gmail.com"

def sendmail(courseId, assignmentTitle, subjectObj, subDate):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    html_content = "<html><body><h4>Check out new assignment of "+ subjectObj.SubjectFullname +" submission last date is "+ subDate +".</h4> <p>Thanks and regards<br>Online College assignment system.</p></body></html>"

    course = Course.objects.get(id=courseId)
    all_user = UserDetail.objects.filter(course = course)
    for i in all_user:
        sender = {"name":"College Assignment System","email":SENDEREMAIL}
        to = [{"email":str(i.user.username),"name":(i.user.first_name)}]
        reply_to = {"email":SENDEREMAIL,"name":"College Assignment System"}
        headers = {"Some-Custom-Name":"unique-id-1234"}
        params = {"parameter":"My param value","subject":(assignmentTitle + " assignment uploaded.")}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=(assignmentTitle + " assignment uploaded."))

        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)