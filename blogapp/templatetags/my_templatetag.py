from django import template
from ..models import Post


register = template.Library()


@register.inclusion_tag('blogapp/sidebars.html')
def sidebar_results():
    posts = Post.objects.all().order_by('-date')[:5]
    return {'posts': posts}
