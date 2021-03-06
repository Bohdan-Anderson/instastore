from django.shortcuts import render_to_response
from django.template import RequestContext
import shopify
from shopify_app.decorators import shop_login_required

def welcome(request):
    return render_to_response('home/welcome.html', {
        'callback_url': "http://%s/login/finalize" % (request.get_host()),
    }, context_instance=RequestContext(request))

@shop_login_required
def index(request):
    # products = shopify.Product.find(limit=3)
    # orders = shopify.Order.find(limit=3, order="created_at DESC")
    pages = shopify.Page.find()
    out = dir(pages[0])

    for page in pages:
        if page.title == "instagram":
            page.body_html = "This is from the app";
            page.save()

    return render_to_response('home/index.html', {
        # 'products': products,
        # 'orders': orders,
        'pages':pages,
        'out':out
    }, context_instance=RequestContext(request))

def design(request):
    return render_to_response('home/design.html', {},
                              context_instance=RequestContext(request))
