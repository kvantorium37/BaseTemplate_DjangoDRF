from app.urls.docs import get_api_docs_urls

api_version = 'v1'
app_name = f'api_{api_version}'
schema_view_urlpatterns = get_api_docs_urls(api_version)  # type: ignore

urlpatterns = [
    # Provide API endpoints here using path and include from django.urls
] + schema_view_urlpatterns
