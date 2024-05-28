from django.forms import ModelForm , forms
from .models import ThesisProject, Supervisor, Student



class SupervisorForm(ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'

    def clean_supervisor_id(self):
        supervisor_id = self.cleaned_data.get('supervisor_id')
        if supervisor_id < 0:
            raise forms.ValidationError("Supervisor ID cannot be negative.")
        return supervisor_id

    




class ThesisProjectForm(ModelForm):
    class Meta:
        model = ThesisProject
        fields = '__all__'

    def clean_topic_num(self):
        topic_num = self.cleaned_data.get('topic_num')
        if topic_num < 0:
            raise forms.ValidationError("Topic number cannot be negative.")
        return topic_num

        

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if student_id < 0:
            raise forms.ValidationError("Student ID cannot be negative.")
        return student_id
    