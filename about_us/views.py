def about_us(request):
    # View for about-us page
    users = User.objects.all()
    ctx = {'users': users}
    return render(request, 'about_us.html', ctx)