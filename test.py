#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'

def make_docx(dict=None):
    from docxtpl import DocxTemplate

    doc = DocxTemplate("export.docx")
    context = {'paper_num': "用户名1",
               'project_name': "用户名2",
               'to_mail': "用户名3",
               'data_selected': "用户名4",
               'proposer': "用户名5",
               'commit_date': "用户名6",
               }
    doc.render(context)
    doc.save("temp_store.docx")


make_docx()