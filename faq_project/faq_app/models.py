from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translation(self, lang='en'):
        if lang == 'hi':
            return {
                'question': self.question_hi or self.question,
                'answer': self.answer_hi or self.answer,
            }
        elif lang == 'bn':
            return {
                'question': self.question_bn or self.question,
                'answer': self.answer_bn or self.answer,
            }
        return {'question': self.question, 'answer': self.answer}

    def save(self, *args, **kwargs):
        # Auto translate when saving
        if not self.question_hi:
            self.question_hi = self.translate(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate(self.question, 'bn')
        if not self.answer_hi:
            self.answer_hi = self.translate(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate(self.answer, 'bn')
        super().save(*args, **kwargs)

    def translate(self, text, lang):
        
        translator = Translator()
        translated = translator.translate(text, dest=lang)
        return translated.text

    def __str__(self):
        return self.question
