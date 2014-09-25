##################################################################################
#    Copyright (c) 2004-2009 Utah State University, All rights reserved.
#    Portions copyright 2009 Massachusetts Institute of Technology, All rights reserved.
#                                                                                 
#    This program is free software; you can redistribute it and/or modify         
#    it under the terms of the GNU General Public License as published by         
#    the Free Software Foundation, version 2.                                      
#                                                                                 
#    This program is distributed in the hope that it will be useful,              
#    but WITHOUT ANY WARRANTY; without even the implied warranty of               
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                
#    GNU General Public License for more details.                                 
#                                                                                 
#    You should have received a copy of the GNU General Public License            
#    along with this program; if not, write to the Free Software                  
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA    
#                                                                                 
##################################################################################

__author__  = '''Brent Lambert, David Ray, Jon Thomas, Shane Graber'''
__version__   = '$ Revision 0.0 $'[11:-2]


from plone.app.layout.viewlets.content import DocumentActionsViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class BookmarkletsActionsViewlet(DocumentActionsViewlet):

    def getSites(self):
        """ returns bookmarking sites. """

        page = self.aq_parent
        page_url = page.absolute_url()
        page_title = page.title.replace(' ', '+')
        page_descr = page.Description()

        available_sites = []
        sites = []       

        props = getToolByName(context, 'portal_properties').bookmarklets_properties
#        is faster than
#        props = self.context.portal_url.portal_properties.bookmarklets_properties
        available_sites = props.available_sites 

        for x in available_sites: 
            sites.append(getattr(props, x)) 
        return sites

    def getSiteUrl(self, site):
        """replace some parts of the site url with title and other from the 
        context"""
        
        url = self.context.absolute_url()
        encodedTitle = self.context.Title().replace(' ', '+')
        pageDescription = self.context.Description()
        site = site.replace('URL', url).replace('ENCODED_TITLE', encodedTitle)
        site = site.replace('DESCR', pageDescription)
        return site

    render = ViewPageTemplateFile("bookmarklets_document_actions.pt")
