from django.conf.urls import include, url

urlpatterns = [
    url(r'^bookmarks/', include('cab.urls.bookmarks')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^feeds/', include('cab.urls.feeds')),
    url(r'^languages/', include('cab.urls.languages')),
    url(r'^popular/', include('cab.urls.popular')),
    url(r'^search/', include('cab.urls.search')),
    url(r'^snippets/', include('cab.urls.snippets')),
    url(r'^tags/', include('cab.urls.tags')),
    url(r'^users/', include('cab.urls.users')),
]
