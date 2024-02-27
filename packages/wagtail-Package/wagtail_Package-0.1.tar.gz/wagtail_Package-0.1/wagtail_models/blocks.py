from django import forms
from django.db import models
from wagtail import blocks as wagtailcoreblocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel

RICHTEXT_BLOCKTYPES = ['superscript','subscript','bold','italic','h2','h3','h4','h5','h6','ul','ol','hr','embed','link','document-link','image']

class YouTubeBlock(wagtailcoreblocks.StructBlock):
    video_id = wagtailcoreblocks.CharBlock()

    class Meta:
        template = "wagtail_pages/blocks/youtube.html"
        icon = "media"
        
class ImageFormatChoiceBlock(wagtailcoreblocks.FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))

class ImageCarouselBlock(wagtailcoreblocks.StructBlock):
    image = ImageChooserBlock()
    caption = wagtailcoreblocks.TextBlock(required=False)
 
    class Meta:
        icon = 'image'

class PullQuoteBlock(wagtailcoreblocks.StructBlock):
    quote = wagtailcoreblocks.TextBlock("quote title")
    attribution = wagtailcoreblocks.CharBlock()

    class Meta:
        icon = "openquote"

class WellBlock(wagtailcoreblocks.StructBlock):
    content = wagtailcoreblocks.RichTextBlock(features=RICHTEXT_BLOCKTYPES)
    color = wagtailcoreblocks.CharBlock(default="grey", required= False)
    background_color = wagtailcoreblocks.CharBlock(default="black", required= False)

class ImageBlock(wagtailcoreblocks.StructBlock):
    image = ImageChooserBlock()
    caption = wagtailcoreblocks.CharBlock(required=False)

    class Meta:
        template = "wagtail_pages/blocks/image.html"
        icon = "image"
    

class ImageTextBlock(wagtailcoreblocks.StructBlock):
    image = ImageChooserBlock()
    description = wagtailcoreblocks.RichTextBlock(features=RICHTEXT_BLOCKTYPES)

class DemoStreamBlock(wagtailcoreblocks.StreamBlock):
    h2 = wagtailcoreblocks.CharBlock(icon="title", classname="title")
    h3 = wagtailcoreblocks.CharBlock(icon="title", classname="title")
    h4 = wagtailcoreblocks.CharBlock(icon="title", classname="title")
    intro = wagtailcoreblocks.RichTextBlock(icon="pilcrow", features=['bold', 'italic', 'link', 'ol', 'ul'])
    rich_text = wagtailcoreblocks.RichTextBlock(icon="pilcrow", features=RICHTEXT_BLOCKTYPES)
    youtube = YouTubeBlock()
    pullquote = PullQuoteBlock()
    full_width_image = ImageBlock(icon="image")
    well = WellBlock(icon="placeholder")
    gallery = wagtailcoreblocks.ListBlock(ImageCarouselBlock(), template = "wagtail_pages/blocks/gallery.html", label="Gallery")
    image_text = wagtailcoreblocks.ListBlock(ImageTextBlock(), template = "wagtail_pages/blocks/image_text.html",icon="image")

class SimpleStreamBlock(DemoStreamBlock):
    pass
    # class Meta:
    #     icon = "placeholder"
    #     template = "wagtail_pages/blocks/streamfield.html"


class DocumentBlock(wagtailcoreblocks.StructBlock):
    title = wagtailcoreblocks.CharBlock()
    document = DocumentChooserBlock(icon="doc-full-inverse")
    documentType = wagtailcoreblocks.ChoiceBlock(choices=(('PresentationSlides','Presentation Slides'), ('Report','Report'), ('Proceedings','Proceedings'), ('Feedback','Feedback'), ('Other', 'Other')),label='Document Type',required= False)
class PageBlock(wagtailcoreblocks.StructBlock):
    title = wagtailcoreblocks.CharBlock()
    page = wagtailcoreblocks.PageChooserBlock(icon="doc-full")


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        FieldPanel('link_document'),
    ]

    class Meta:
        abstract = True

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True