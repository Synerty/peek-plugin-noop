'''
Created on 17/06/2013

@author: darkstar
'''

from old.ElementUtil import RapuiElement, addPageElement


@addPageElement('')
@addPageElement('peekadm/setting')
@addPageElement('peekadm/update')
class ContentElement(RapuiElement):
    xmlFileName = 'NoopAdmAppTemplate.xml'
