cloudpy_org_version='1.4.4'
gsep = {'user_email_sep': '-0-', '@': '-1-', '.': '-2-'}
from cloudpy_org_base.tools import processing_tools
from cloudpy_org_base.docs import auto_document,convert_jupiter_notebook_to_html,documentation_from_folder
from cloudpy_org_base.aws import aws_framework_manager,aws_framework_manager_client,gen_aws_auth_token,gen_new_service_token,configure_aws,get_my_aws_service_token
#from cloudpy_org_base.web import flask_website
#from cloudpy_org_base.imgedit import colors