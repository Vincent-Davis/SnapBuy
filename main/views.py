from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Royale Pass',
        'price': 80000,
        'description': 'CR GG EZ WIN, Overlevel everyone!',
        'produk_terjual' : 0,
        'rating' : 0.01,
    }

    return render(request, "main.html", context)

