from django import forms
from .models import Question , Answer


class QuestionForm(forms.ModelForm):
    question = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class':'form-floating form-control w-75 m-3 p-3','placeholder':'Add Your Question here Like "What" , "How" , "Where" , "Why" etc.'}),
        )


    class Meta:
        model = Question
        fields = ('question',)



class AnswerForm(forms.Form):
    ans = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class':'form-floating form-control w-50','placeholder':'Write Your Thought Here.'}),
        )


    class Meta:
        model = Answer
        fields =('ans',)

    def save(self, commit=True):
        answer = Answer(ans=self.cleaned_data['ans'])
        if commit:
            answer.save()
        return answer
        
    