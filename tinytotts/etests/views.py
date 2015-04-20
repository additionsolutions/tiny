from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from etests.models import TestSet, TestSetLine, Answer
from django.db.models import Q, Max, Min
from contents.models import User


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
            
    record = "normal"   
    # # Find a First and Last questions
    Record_obj = TestSetLine.objects.filter(testset=request.session['testno'])
    # # Calculates the maximum and minimum out of the already-retrieved objects
    last = Record_obj.aggregate(Max('srno'))
    first = Record_obj.aggregate(Min('srno'))   
            
    if action == 2: # Next
        sr = request.session['qno'] + 1
    if action == 1: # Previous
        sr = request.session['qno'] - 1
        
    testsetline = "etests/" + str(TestSetLine.objects.get(Q(srno=sr), Q(testset=request.session['testno'])))
    request.session['qno'] = sr
    
    # find out if first or last record
    if sr == last['srno__max']:
        record = "last"
        
    if sr == first['srno__min']:
        record = "first"

    return render(request, 'etests/test_area.html', { 'testsetline': testsetline,'record': record})


## Evaluate and give marks
def etestans(request, ans):
    if request.method == 'GET':
        try:
            ans = int(ans)
        except ValueError:
            raise Http404()
            
    q = TestSetLine.objects.get(Q(srno=request.session['qno']), Q(testset=request.session['testno']))

    try:
        ansr = Answer.objects.get(question=q)
    except Answer.DoesNotExist:
        ansr = Answer.objects.create(marks=ans, question=q, user=request.user)
    else:
        ansr.marks = ans
        ansr.user = request.user

    ansr.save()
    # Answer.objects.all().delete()            
    
    answer = "Answer recorded"
    return render(request, 'etests/ans_area.html', { 'answer': answer })