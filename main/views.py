from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Panci',
        'price': '5000',
        'description': 'Panci buat mentung orang',
        'quantity': '10',
        'category': 'Dapur',
        'featured': True
    }

    return render(request, "main.html", context)
