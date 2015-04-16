from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from etests.models import TestSet, TestSetLine

def etest(request):
    #srno = request.GET.get('sr', '1')
    #testsetline = "{% include 'etests/" + str((TestSetLine.objects.get(srno=srno))) + "' %}" 
    return render(request, 'etests/etest.html')
    
def etestsr(request, sr):
    if request.method == 'GET':
        try:
            sr = int(sr)
        except ValueError:
            raise Http404()
            
    testsetline = "etests/" + str(TestSetLine.objects.get(srno=sr))       
    return render(request, 'etests/test_area.html', { 'testsetline': testsetline })
