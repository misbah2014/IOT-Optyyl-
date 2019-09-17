from tableau_tools import *
from tableau_tools.tableau_rest_api import *

t = TableauRestApiConnection26(u"http://dashboard.crgroup.com", u"himanshu", u"himanshu123", site_content_url=u"Finance")
print(t)
t.signin()
logger = Logger(u"log_file.txt")
t.enable_logging(logger)
groups = t.query_groups()
groups_dict = t.convert_xml_list_to_name_id_dict(groups)
print(groups)

