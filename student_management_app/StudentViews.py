from django.shortcuts import render


def student_home(request):
    return render(request,"student_template/student_home_template.html")

# def student_feedback(request):
#     staff_id=Students.objects.get(admin=request.user.id)
#     feedback_data=FeedBackStudent.objects.filter(student_id=staff_id)
#     return render(request,"student_template/feedback.html")

# def student_feedback_save(request):
#     if request.methods != 'POST':
#         return HttpResponseRedirect(reverse('student_feedback'))
#     else:
#         feedback_msg = request.POST.get('feedback_msg')

#         student_obj = students.objects.get(admin=request.user.id)
#         try:
#             feedback=FeedBackStudent(student_id=staff_obj,feedback=feedback_msg,feedback_reply='')