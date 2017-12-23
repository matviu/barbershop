from django import template
from chunks.models import Chunk

register = template.Library()

@register.simple_tag()
def chunk(title):
	chunk = Chunk.objects.get(title=title)
	return chunk.content