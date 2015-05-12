from django.shortcuts import render, redirect, get_object_or_404, RequestContext, render_to_response
from etests.models import TestSet, TestSetLine, Answer
from django.forms import ModelForm, ModelChoiceField, HiddenInput
from django.db.models import Q, Max, Min
from contents.models import User
from .forms import TestSetForm, TestSetLineForm

######################################
# Test Set for Admin
######################################


def testset(request, template_name='etests/testset_list.html'):
    testset = TestSet.objects.all()
    data = {}
    data['object_list'] = testset
    return render(request, template_name, data)
    
def testset_create(request, template_name='etests/testset_form.html'):
    form = TestSetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('testset_list')
    return render(request, template_name, {'form':form})

def testset_update(request, pk, template_name='etests/testset_form.html'):
    testset = get_object_or_404(TestSet, pk=pk)
    form = TestSetForm(request.POST or None, instance=testset)
    if form.is_valid():
        form.save()
        return redirect('testset_list')
    return render(request, template_name, {'form':form})

def testset_delete(request, pk, template_name='etests/testset_confirm_delete.html'):
    testset = get_object_or_404(TestSet, pk=pk)
    if request.method=='POST':
        testset.delete()
        return redirect('testset_list')
    return render(request, template_name, {'object':testset})
 
    
    
def testq(request, template_name='etests/testquestion_list.html'):
    testsetline = TestSetLine.objects.all()
    data = {}
    data['object_list'] = testsetline
    return render(request, template_name, data)

def testsetline_update(request, pk, template_name='etests/testset_form.html'):
    testsetline = get_object_or_404(TestSet, pk=pk)
    form = TestSetLineForm(request.POST or None, instance=testsetline)
    if form.is_valid():
        form.save()
        return redirect('testquestion_list')
    return render(request, template_name, {'form':form})

def testsetline_delete(request, pk, template_name='etests/testset_confirm_delete.html'):
    testsetline = get_object_or_404(TestSet, pk=pk)
    if request.method=='POST':
        testsetline.delete()
        return redirect('testquestion_list')
    return render(request, template_name, {'object':testsetline})

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
    
######################################
# TestSet and TestSetLine using technique described at :
# https://collingrady.wordpress.com/2008/02/18/editing-multiple-objects-in-django-with-newforms/
######################################   
    
    
def add_testset(request):
    if request.method == "POST":
        tsform = TestSetForm(request.POST, instance=TestSet())
        tslforms = [TestSetLineForm(request.POST, prefix=str(x), instance=TestSetLine()) for x in range(0,3)]
        if tsform.is_valid() and all([tslf.is_valid() for tslf in tslforms]):
            new_testset = tsform.save()
            for tsl in tslforms:
                new_testsetline = tsl.save(commit=False)
                new_testsetline.testset = new_testset
                new_testsetline.save()
            return HttpResponseRedirect('/etest/add/')
    else:
        tsform = TestSetForm(instance=TestSet())
        tslforms = [TestSetLineForm(prefix=str(x), instance=TestSetLine()) for x in range(0,3)]
    return render_to_response('etests/add_testset.html', {'p_form': tsform, 'c_forms': tslforms})