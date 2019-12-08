import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi

from config import Configuration

# Get App key and App SID from https://cloud.aspose.com
pdf_api_client = asposepdfcloud.api_client.ApiClient(
    app_key='1d0f2d902326f23e3eb51ba5a00497b7',
    app_sid='66924cc5-8896-4380-b872-e415a234fde4')

pdf_api = PdfApi(pdf_api_client)


# filename = '../uploads' + "/"+'ikzrttmknhgmdhhmovii.pdf'
# remote_name = '02_pages.pdf'
# copied_file= '02_pages_new.pdf'
# #upload PDF file to storage
# pdf_api.upload_file(remote_name,filename)
#
# #upload PDF file to storage
# pdf_api.copy_file(remote_name,copied_file)
#
# #Replace Text
# text_replace = asposepdfcloud.models.TextReplace(old_value='asdf@email.com',new_value='<<email>>',regex='true')
# text_replace_list = asposepdfcloud.models.TextReplaceListRequest(text_replaces=[text_replace])
#
# response = pdf_api.post_document_text_replace(copied_file, text_replace_list)
# file = pdf_api.download_file('02_pages_new.pdf')
# print(file)

def get_replacer(old, new):
    return asposepdfcloud.models.TextReplace(old_value=old, new_value=new, regex='true')


def replace_file(replace_lst, base_file_name):
    upload_name = Configuration.UPLOAD_FOLDER + "/" + base_file_name + ".pdf"
    pdf_api.upload_file(base_file_name+"remote" + ".pdf", upload_name)
    text_replace_list = asposepdfcloud.models.TextReplaceListRequest(text_replaces=replace_lst)
    response = pdf_api.post_document_text_replace(base_file_name+"remote" + ".pdf", text_replace_list)
    file = pdf_api.download_file(base_file_name+"remote" + ".pdf")
    return file
