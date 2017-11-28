from django.http import HttpResponse
from django.shortcuts import render_to_response

def show_code(request):
    if request.method == "POST":
        instr = request.POST['instr']
        
        outstr = ""
        detail = ""
        for ch in instr:
            outstr += "/u%04x" % ord(ch)
            detail += ch + "(" + "/u%04x" % ord(ch) + ")"
        return render_to_response("page.html", {'output': outstr,
                                                'instr': instr,
                                                'detail': detail})
    return render_to_response("page.html", {})
