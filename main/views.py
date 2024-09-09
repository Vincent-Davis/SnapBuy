from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Vincent Davis Leonard Tjoeng',
        'kelas': 'F',
        'aplikasi' : 'SnapBuy'
    }

    return render(request, "main.html", context)

