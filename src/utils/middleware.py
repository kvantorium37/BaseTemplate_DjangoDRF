import logging
import time

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):
    """Middleware that logs every request with info about user."""

    def process_request(self, request):
        """Save start time at request."""
        request.start_time = time.time()

    def process_response(self, request, response):
        """Write request info to logs."""
        user_ip = (
            request.META.get('HTTP_X_FORWARDED_FOR')
            or request.META.get('REMOTE_ADDR')
        )

        user_id_label = (
            f' (ID: {request.user.id})'
            if request.user.id
            else ''
        )

        run_time = time.time() - request.start_time

        logger.info(
            '"IP: %s" "User: %s%s" "%s %s" "Response status: %s" '
            '"Run time: %.2f sec"',
            user_ip,
            request.user,
            user_id_label,
            request.method,
            request.build_absolute_uri(),
            response.status_code,
            run_time,
        )

        return response
