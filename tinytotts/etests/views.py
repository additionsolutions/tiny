from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from etests.models import TestSet, TestSetLine
from django.db.models import Q


######################################
# Test List for selected group
######################################
def testlist(request):
    context = RequestContext(request)
    testlist = []
    if request.method == 'GET':
        testlist = TestSet.objects.filter(groups=request.user.groups.all())
        
    return render_to_response('etests/testlist.html', {'testlist': testlist }, context)


## Start with first question  
def etest(request, testset):
    testset_obj = TestSet.objects.get(id=testset)
    request.session['testno'] = testset
    request.session['qno'] = 0
    
    return render(request, 'etests/etest.html', { 'testset': testset_obj })
    
    
## Navigate   
def etestsr(request, action):
    if request.method == 'GET':
        try:
            action = int(action)
        except ValueError:
            raise Http404()
    if action == 2: # Next
        sr = request.session['qno'] + 1
    if action == 1: # Previous
        sr = request.session['qno'] - 1
        
    testsetline = "etests/" + str(TestSetLine.objects.get(Q(srno=sr), Q(testset=request.session['testno'])))
    request.session['qno'] = sr
    return render(request, 'etests/test_area.html', { 'testsetline': testsetline })


## Evaluate and give marks
def etestans(request, ans):
    if request.method == 'GET':
        try:
            ans = int(ans)
        except ValueError:
            raise Http404()
    
    testsetline = request.session['qno']
    
    return render(request)