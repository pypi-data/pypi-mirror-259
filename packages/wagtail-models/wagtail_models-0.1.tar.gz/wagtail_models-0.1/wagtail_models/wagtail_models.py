from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.models import Orderable, Page
from wagtail.search import index
from modelcluster.fields import ParentalKey
from django.core.validators import MinValueValidator
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core import blocks

class StandardIndexPage(Page):
    '''This is models for the Index page and which '''
    body = RichTextField(blank=True)
    priority_index=models.PositiveIntegerField(default=0)
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def get_context(self,request):
        context = super(StandardIndexPage, self).get_context(request)
        context['child_page']=StandardPage.objects.child_of(self).live().order_by('title').public()
        context['page']=self
        return context
    
      
StandardIndexPage.content_panels = [
    FieldPanel('title'),
    FieldPanel('body'),
    FieldPanel('priority_index'),
]

TEMPLATE_CHOICES = [
    ('wagtail_pages/alternative_layout.html', 'Alternative Layout'),
]
class StandardPage(Page):
    parent_page_types = ['wagtail_pages.StandardIndexPage']
    small_introduction=models.CharField(max_length=255, blank=False)
    body = StreamField(SimpleStreamBlock(), use_json_field=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    alternative_template = models.CharField(max_length=250, choices=TEMPLATE_CHOICES, blank=True, null=True) 
    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def get_template(self, request):
        if self.alternative_template:
            return self.alternative_template
        return super().get_template(request)
    
    def get_context(self,request):
        if self.alternative_template == 'wagtail_pages/alternative_layout.html':
            context = super(StandardPage, self).get_context(request)
            context['note'] = 'This is a note from the StandardPage model for alternative layout.'
            return context
        context = super(StandardPage, self).get_context(request)
        return context
       

StandardPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('alternative_template'),
    FieldPanel('body'),
    FieldPanel('small_introduction'),
    FieldPanel('featured_image'),
    InlinePanel('standard_page_related_link', label="Related Content"),
]

class StandardPageRelatedLink(Orderable):
    page = ParentalKey('wagtail_pages.StandardPage', related_name='standard_page_related_link', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField(blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]

