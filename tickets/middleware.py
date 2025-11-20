from django.shortcuts import redirect

class ProfileCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Paths that do not require a profile
        allowed_paths = ['/', '/login/', '/create_profile/']

        # Allow access to admin, static, and media files
        if request.path.startswith('/admin/') or request.path.startswith('/static/') or request.path.startswith('/media/'):
            return self.get_response(request)

        if request.path not in allowed_paths and not request.session.get('has_profile'):
            return redirect('login')

        response = self.get_response(request)
        return response
